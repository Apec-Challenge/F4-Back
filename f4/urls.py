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
from funding.views import (
    FundingUpdateAPIView, FundingDeleteAPIView, FundingViewSet )
from review.viewsets import ReviewListViewSet, ReviewUpdateViewSet, ReviewDeleteViewSet
from accounts import views as acc_views
from allauth.account.views import confirm_email
from django.conf.urls.static import static
from django.conf import settings
from place.viewsets import PlaceViewSet,PlaceDeleteAPIView, PlaceCreateAPIView, PlaceUpdateAPIView
from accounts.views import MoneyRechargeViewSet, UserListViewSet
from place import views
from funding.views import FundingLike
from review.views import ReviewLike
router = routers.DefaultRouter()
router.register('funding', FundingViewSet, basename='funding')
router.register('place',PlaceViewSet,basename='place')
router.register('review', ReviewListViewSet)
router.register('user', UserListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(acc_urls)),
    path('api/', include(router.urls)),
    url('api/review/update/(?P<id>[\w-]+)/$', ReviewUpdateViewSet.as_view(), name='review_update'),
    url('api/review/delete/(?P<id>[\w-]+)/$', ReviewDeleteViewSet.as_view(), name='review_delete'),
    url('api/funding/(?P<id>[\w-]+)/edit/$', FundingUpdateAPIView.as_view(), name='funding_update'),
    url('api/funding/(?P<id>[\w-]+)/delete/$', FundingDeleteAPIView.as_view(), name='funding_delete'),
    path('accounts/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    url(r'^', include('django.contrib.auth.urls')),
    url('api/place/$', PlaceViewSet),
    url('api/place/(?P<place_id>[\w-]+)/delete/$',PlaceDeleteAPIView.as_view(),name='place_delete'),
    url('api/place/(?P<place_id>[\w-]+)/update/$', PlaceUpdateAPIView.as_view(), name='place_update'),
    url('api/recharge/(?P<id>[\w-]+)/$', MoneyRechargeViewSet.as_view(), name='money_recharge'),
    path('place_like/<str:user>/<str:q>/', views.PlaceLike),
    path('review_like/<str:user>/<int:id>/', ReviewLike),
    path('funding_like/<str:user>/<int:id>/', FundingLike),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


