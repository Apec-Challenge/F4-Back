from django.shortcuts import render, redirect
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
from django.conf import settings
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

BASE_URL = 'http://127.0.0.1:8000/'

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://127.0.0.1:8000/accounts/github/login/'

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = BASE_URL + 'rest-auth/google/callback/'


class CustomLoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        mydata = {"pk" : self.user.pk, "email": self.user.email, "nickname": self.user.nickname}
        response.data.update(mydata)
        return response

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSeriializer


def google_login(request):
    client_id = getattr(settings, 'GOOGLE_CLIENT_ID')
    redirect_uri = BASE_URL + "rest-auth/google/callback/"
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A//www.googleapis.com/auth/drive.metadata.readonly&include_granted_scopes=true&response_type=token&client_id={client_id}&redirect_uri={redirect_uri}"
    )

# def google_callback(request):
#     # return redirect('../index/')