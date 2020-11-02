from django.db import models
from django.db.models import Count, F, Avg, Sum


PERSON_HYGIENE_CHOICES = (
    (0, '1'),
    (1, '2'),
    (2, '3'),
    (3, '4'),
    (4, '5'),
)
SANITIZER_CHOICES = (
    (0, '1'),
    (1, '2'),
    (2, '3'),
    (3, '4'),
    (4, '5'),
)
BODY_TEMPERATURE_CHECK_CHOICES = (
    (0, '1'),
    (1, '2'),
    (2, '3'),
    (3, '4'),
    (4, '5'),
)


class Place(models.Model):
    # Place model 
    place_id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=50,null=True,)
    place_image = models.ImageField(upload_to="place/img/", blank=False, null=True,)
    description = models.CharField(max_length=1000, blank=True, null=True,)
    address = models.CharField(max_length=10000,null=True,)
    lng = models.CharField(max_length=50, null=True)
    lat = models.CharField(max_length=50, null=True)
    hand_sanitizer = models.PositiveIntegerField(choices=SANITIZER_CHOICES,default=2)
    person_hygiene = models.PositiveIntegerField(choices=PERSON_HYGIENE_CHOICES,default=2)
    body_temperature_check = models.PositiveIntegerField( choices=BODY_TEMPERATURE_CHECK_CHOICES, default=2)
    counts = models.PositiveIntegerField(default=0, null=True,)
    #  likes = models.ManyToManyField(User, related_name='place_likes', default=None, blank=True)

    # place모델 필드 추가
    @property
    def total_likes(self):
        return self.user_likes.count()

    @property
    def reviews_count(self):
        from review.models import Review
        cnt = Review.objects.filter(place=self.place_id).count()
        return cnt

    @property
    def reviews_sum(self):
        from review.models import Review
        sums = Review.objects.filter(place=self.place_id).aggregate(Sum('rating'))
        sum = sums.get('rating__sum')
        return sum

    @property
    def review_average(self):
        sum = self.reviews_sum
        cnt = self.reviews_count
        if cnt == 0:
            avg = 0
        else:
            avg = round(float(sum/cnt),1)
        return avg
