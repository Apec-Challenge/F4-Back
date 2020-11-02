from rest_framework import serializers
from .models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model = Review
        fields = ('id', 'user', 'username', 'place', 'content', 'created_at', 'updated_at', 'rating', 'total_likes', 'user_likes')


class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content', 'rating')


class ReviewDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

