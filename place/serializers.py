from rest_framework import serializers
from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class PlacePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('place_id', 'title', 'place_image', 'description', 'address', 'lng', 'lat', 'person_hygiene', 'hand_sanitizer',
                  'body_temperature_check', 'counts', 'total_likes','user_likes', 'review_average')



class PlaceLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'