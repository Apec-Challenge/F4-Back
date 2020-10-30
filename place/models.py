from django.db import models
from django.utils.translation import ugettext_lazy as _
from review.models import Review
from django.db.models import Count, Avg, Min, Max, Sum

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


class Place(models.Model):
    # Place model 
    place_id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=30,null=True,)
    place_image = models.ImageField(upload_to="place/img/", blank=True, null=True,)
    description = models.CharField(max_length=100, blank=True, null=True,)
    address = models.CharField(max_length=10000,null=True,)
    lng = models.CharField(max_length=50,blank=True,null=True)
    lat = models.CharField(max_length=50,blank=True,null=True)
    hand_sanitizer = models.PositiveIntegerField(choices=SANITIZER_CHOICES,default=2)
    person_hygiene = models.PositiveIntegerField(choices=PERSON_HYGIENE_CHOICES,default=2)
    body_temperature_check = models.PositiveIntegerField( choices=BODY_TEMPERATURE_CHECK_CHOICES ,default=2)
    counts = models.PositiveIntegerField(default=0,null=True,)
    #  likes = models.ManyToManyField(User, related_name='place_likes', default=None, blank=True)

    def count_likes(self):
        # total likes_user
        return self.user_likes.count()

    @property
    def avg_ppe(self):
        # average ppe score
        score = (self.Mask + self.person_hygiene + self.body_temperature_check)/3
        return round(score,2)



