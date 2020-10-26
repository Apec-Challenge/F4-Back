from rest_framework import serializers
from .models import Place, GooglePlace, PPE

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
