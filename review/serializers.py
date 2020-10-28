from rest_framework import serializers
from .models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content', 'place', 'created_at', 'updated_at', 'rating')


class ReviewDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

