from django.db import models
from accounts.models import User
from place.models import Place


class Funding(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # owner_user = models.ForeignKey(Owner_User, on_delete=models.CASCADE, blank=True)
    # consumer_user = models.ForeignKey(Consumer_User, on_delete=models.CASCADE, blank=True)
    funding_price = models.PositiveIntegerField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.place.title + ': ' + self.funding_price
