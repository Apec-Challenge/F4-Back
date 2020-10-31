from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('rest-auth/login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('rest-auth/registration/', views.CustomRegisterView.as_view(), name='custom_registration'),
    path('rest-auth/google/', views.google_login, name='google_login'),
    path('rest-auth/google/callback/', views.google_callback, name='google_callback'),
    path('rest-auth/google/login/', views.GoogleLogin.as_view(), name='google'),
      # url(r'^rest-auth/google/login/$', views.GoogleLogin.as_view(), name='fb_login')
    path('rest-auth/kakao/login/', views.kakao_login, name='kakao_login'),
    path('rest-auth/kakao/callback/', views.kakao_callback, name='kakao_call'),

]