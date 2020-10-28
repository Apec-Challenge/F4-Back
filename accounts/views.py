from django.shortcuts import render
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter, GitHubProvider
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from allauth.socialaccount.providers.github.views import oauth2_callback
from .serializers import CustomRegisterSeriializer
from rest_framework import viewsets
from .models import User

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://127.0.0.1:8000/accounts/github/login/'


class CustomLoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        mydata = {"pk" : self.user.pk, "email": self.user.email, "nickname": self.user.nickname}
        response.data.update(mydata)
        return response

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSeriializer
