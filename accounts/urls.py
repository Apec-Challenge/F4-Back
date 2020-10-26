from django.urls import path
from django.conf.urls import url
from . import views

from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)

urlpatterns = [
    # path('github/', views.GithubLogin.as_view(), name='a'),
    url(r'^rest-auth/github/$', views.GithubLogin.as_view(), name='github_login'),
    url(r'^github/connect/$', views.GithubConnect.as_view(), name='github'),
    url(r'^socialaccounts/(?P<pk>\d+)/disconnect/$', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),
    # url(r'^socialaccounts/$', SocialAccountListView.as_view(), name='social_account_list'),
]