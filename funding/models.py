from django.db import models
from accounts.models import User
from place.models import Place


class Funding(models.Model):
    thumbnail_image = models.ImageField(models.ImageField(default="",blank=True, null=True, upload_to="blog/%Y/%m/%d"))
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    user = models.ManyToManyField(User, blank=True)
    content_image = models.ImageField(models.ImageField(default="",blank=True, null=True, upload_to="blog/%Y/%m/%d"))
    content_text = models.TextField(blank=True)
    funding_goal_amount = models.PositiveIntegerField(null=False,default=0)
    funding_amount = models.PositiveIntegerField(null=False,default=0)
    like_count = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.title
