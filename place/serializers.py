from rest_framework import serializers
from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class PlacePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('place_id', 'title', 'img', 'description', 'location', 'lng', 'lat', 'Mask', 'hand_sanitizer', 'disposable_gloves')


class PlaceLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = 'count_likes'