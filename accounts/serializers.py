from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from django.utils.translation import ugettext_lazy as _
class CustomRegisterSeriializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=10)

    def get_cleaned_data(self):
        return_value = super().get_cleaned_data()
        add_value = {'nickname': self.validated_data.get('nickname', '')}
        return_value.update(add_value)
        return return_value