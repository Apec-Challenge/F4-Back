from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^rest-auth/github/$', views.GithubLogin.as_view(), name='github_login'),
    path('rest-auth/login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('rest-auth/registration/', views.CustomRegisterView.as_view(), name='custom_registration'),
    # path('accounts/github/login/', views.github_callback, name='github_callbasck'),
    path('rest-auth/google/', views.google_login, name='google_login'),
    # path('rest-auth/google/callback/', views.google_callback, name='google_callback'),
    path('rest-auth/google/login', views.GoogleLogin.as_view(), name='google')
]