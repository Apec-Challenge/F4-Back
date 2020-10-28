from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^rest-auth/github/$', views.GithubLogin.as_view(), name='github_login'),
    # url(r'^socialaccounts/$', SocialAccountListView.as_view(), name='social_account_list'),
    path('rest-auth/login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('rest-auth/registration/', views.CustomRegisterView.as_view(), name='custom_registration'),
    # path('accounts/github/login/', views.github_callback, name='github_callbasck'),

]