from rest_framework import serializers
from .models import Funding
from accounts.models import User
from django.utils import timezone


class FundingSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner_user.nickname')
    class Meta:
        model = Funding
        fields = ('id','thumbnail_image', 'place','title', 'description', 'owner_username', 'backed_list', 'content_image', 'content_text', 'funding_goal_amount', 'funding_amount', 'created_at', 'ended_at', 'total_likes' ,'user_likes')


class FundingPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ('image', 'place','title','content', 'funding_price', 'created_at', 'ended_at','total_likes')


class FundingDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = '__all__'
