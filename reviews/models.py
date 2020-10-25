from django.db import models

# Create your models here.


class Review(models.Model):
    # account = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    # place = models.ForeignKey('place.Place', on_delete=models.CASCADE)
    content = models.TextField(blank=False, max_length=1000)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)
    rating = models.FloatField(default=0)

    # def __str__(self):
    #     return self.account.username



