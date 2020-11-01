from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count, F

REVIEW_RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, blank=False)
    place = models.ForeignKey("place.Place", on_delete=models.CASCADE, blank=False)
    content = models.TextField(blank=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    rating = models.FloatField(choices=REVIEW_RATING_CHOICES, blank=False)
    # review_likes = models.ManyToManyField(User, related_name='review_likes', default=None, blank=True)
    # like = models.ManyToManyField(User, related_name='funding_likes',blank=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        from place.models import Place
        if not self.pk:
            Place.objects.filter(pk=self.place_id).update(counts=F('counts') + 1)
        super().save(*args, **kwargs)

    @property
    def total_likes(self):
        return self.user_likes.count()
