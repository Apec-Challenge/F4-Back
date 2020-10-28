from rest_framework import serializers
from .models import Funding
from django.utils import timezone

class FundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = '__all__'


class FundingPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ('image', 'place','title','content', 'funding_price', 'created_at', 'ended_at')


class FundingDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = '__all__'