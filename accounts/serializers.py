from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from django.utils.translation import ugettext_lazy as _
from accounts.models import User


class CustomRegisterSeriializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=10)

    def get_cleaned_data(self):
        return_value = super().get_cleaned_data()
        add_value = {'nickname': self.validated_data.get('nickname', '')}
        return_value.update(add_value)
        return return_value


class UserListSerializer(serializers.ModelSerializer):
    """
    유저 확인하기 위한 테스트 시리얼라이저
    추후에 삭제할 예정
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'nickname', 'money')


class MoneyRechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_type', 'money')


