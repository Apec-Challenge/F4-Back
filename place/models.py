from django.db import models
# from accounts import User

class Place(models.Model):
    # Place model 
    google_api = models.CharField(primary_key=True,max_length=50)
    img = models.ImageField(upload_to="place/", default="Img")
    description = models.CharField(max_length=100, blank=True, null=True,)
    business_hours = models.CharField(max_length=100, blank=True, null=True,)


class GooglePlace(models.Model):
    # google api 사용하여 place 정보 가져오기 위한 모델
    place_id = models.OneToOneField(Place)
    title = models.CharField(max_length=30)
    location = models.CharField(max_length=200,blank=True,)
    lng = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)


class PPE(models.Model):
    # place 모델의 ppe 정보 모델
    place_id = models.OneToOneField(Place)
    # mask
    # gloves
    # disinfection
