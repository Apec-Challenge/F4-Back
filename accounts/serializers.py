from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from funding.serializers import UserFundingSerializer
from accounts.models import User


class CustomRegisterSeriializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=10)

    def get_cleaned_data(self):
        return_value = super().get_cleaned_data()
        add_value = {'nickname': self.validated_data.get('nickname', '')}
        return_value.update(add_value)
        return return_value


class MoneyRechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'money')


class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    backed_list = UserFundingSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','email', 'nickname', 'money', 'place_likes','backed_list')