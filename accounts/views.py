from django.shortcuts import render
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter, GitHubProvider
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView, SocialConnectView
from rest_auth.registration.serializers import SocialLoginSerializer
from allauth.socialaccount.providers.github.views import oauth2_callback

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://127.0.0.1:8000/accounts/github/login/'


class GithubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/github/login/'
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer
