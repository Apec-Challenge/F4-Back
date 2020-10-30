from django.db import models
from django.utils.translation import ugettext_lazy as _
from review.models import Review
from django.db.models import Count, Avg, Min, Max, Sum

SANITIZER_CHOICES = (
    (0, _('Terrible')),
    (1, _('Poor')),
    (2, _('Average')),
    (3, _('Very Good')),
    (4, _('Excellent')),
)
HYGIENE_CHOICES = (
    (0, _('Terrible')),
    (1, _('Poor')),
    (2, _('Average')),
    (3, _('Very Good')),
    (4, _('Excellent')),
)
TEMPERATURE_CHECK_CHOICES = (
    (0, _('Terrible')),
    (1, _('Poor')),
    (2, _('Average')),
    (3, _('Very Good')),
    (4, _('Excellent')),
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
    hand_sanitizer = models.IntegerField(choices=SANITIZER_CHOICES, blank=True, default=2)
    person_hygiene = models.IntegerField(choices=HYGIENE_CHOICES, blank=True, default=2)
    body_temperature_check = models.IntegerField(choices=TEMPERATURE_CHECK_CHOICES, blank=True, default=2)
    #  likes = models.ManyToManyField(User, related_name='place_likes', default=None, blank=True)
    counts = models.PositiveIntegerField(default=0, null=True,)


    def count_likes(self):
        # total likes_user
        return self.likes.count()

    def avg_ppe(self):
        # average ppe score
        score = (self.Mask + self.hand_sanitizer + self.disposable_gloves)/3
        return score



