"""Project_F4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.db import router
from django.urls import path, include
from accounts import urls as acc_urls
from reviews.viewsets import ReviewCreateViewSet, ReviewUpdateViewSet
from funding.views import FundingUpdateAPIView, FundingDeleteAPIView, FundingCreateViewSet, FundingViewSet
from rest_framework import routers
from accounts import views as acc_views
from allauth.account.views import confirm_email
router = routers.DefaultRouter()
router.register('funding', FundingViewSet, basename='funding')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(acc_urls)),
    path('api/', include(router.urls)),
    url('api/funding/(?P<id>[\w-]+)/edit/$', FundingUpdateAPIView.as_view(), name='funding_update'),
    url('api/funding/(?P<id>[\w-]+)/delete/$', FundingDeleteAPIView.as_view(), name='funding_delete'),
    url('api/funding/create/$', FundingCreateViewSet.as_view(), name='funding_create'),
    url('review/(?P<id>[\w-]+)/create/$', ReviewCreateViewSet.as_view(), name='review_create'),
    url('review/(?P<id>[\w-]+)/update/$', ReviewUpdateViewSet.as_view(), name='review_update'),
    path('accounts/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    url(r'^', include('django.contrib.auth.urls')),
]
