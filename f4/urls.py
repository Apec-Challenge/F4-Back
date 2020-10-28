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
from rest_framework import routers
from accounts import urls as acc_urls
from review.viewsets import ReviewListViewSet, ReviewUpdateViewSet, ReviewDeleteViewSet
from accounts import views as acc_views
from allauth.account.views import confirm_email

router = routers.DefaultRouter()
router.register('review', ReviewListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(acc_urls)),
    path('api/', include(router.urls)),
    # url('api/review/create/$', ReviewCreateViewSet.as_view(), name='review_create'),
    url('api/review/update/(?P<id>[\w-]+)/$', ReviewUpdateViewSet.as_view(), name='review_update'),
    url('api/review/delete/(?P<id>[\w-]+)/$', ReviewDeleteViewSet.as_view(), name='review_delete'),
    path('accounts/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    url(r'^', include('django.contrib.auth.urls')),
]
