from django.db import models

MASK_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
SANITIZER_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
DISPOSABLE_GLOVES_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)


class Place(models.Model):
    # Place model 
    place_id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=30,null=True,)
    img = models.ImageField(upload_to="place/img/", blank=True, null=True,)
    description = models.CharField(max_length=100, blank=True, null=True,)
    location = models.CharField(max_length=10000,null=True,)
    lng = models.CharField(max_length=50,blank=True,null=True)
    lat = models.CharField(max_length=50,blank=True,null=True)
    Mask = models.CharField(max_length=10,choices=MASK_CHOICES,default='Dont Know')
    hand_sanitizer = models.CharField(max_length=10, choices=SANITIZER_CHOICES, default='Dont Know')
    disposable_gloves = models.CharField(max_length=10, choices=DISPOSABLE_GLOVES_CHOICES, default='Dont Know')
    #  likes = models.ManyToManyField(User, related_name='place_likes', default=None, blank=True)

    def count_likes(self):
        # total likes_user
        return self.likes.count()

    def avg_ppe(self):
        # average ppe score
        score = (self.Mask + self.hand_sanitizer + self.disposable_gloves)/3
        return score
