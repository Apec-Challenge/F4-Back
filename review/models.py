from django.db import models
from accounts.models import User
from django.utils.translation import ugettext_lazy as _

REVIEW_RATING_CHOICES = (
    ('1', _('Terrible')),
    ('2', _('Poor')),
    ('3', _('Average')),
    ('4', _('Very Good')),
    ('5', _('Excellent')),
)

REVIEW_DEFAULT_ID = 1


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=REVIEW_DEFAULT_ID)
    # place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    rating = models.FloatField(choices=REVIEW_RATING_CHOICES, default=0)

    def __str__(self):
        return self.user.email


