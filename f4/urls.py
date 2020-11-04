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
from funding.viewsets import (
    FundingUpdateAPIView, FundingDeleteAPIView, FundingViewSet ,
    MainFundingViewSet, MainFundingUpdateAPIView, MainFundingDeleteAPIView,
    FundingCommentViewSet, FundingCommentUpdateAPIView, FundingCommentDeleteAPIView,
)
from review.viewsets import ReviewListViewSet, ReviewUpdateViewSet, ReviewDeleteViewSet
from allauth.account.views import confirm_email
from django.conf.urls.static import static
from django.conf import settings
from place.viewsets import PlaceViewSet,PlaceDeleteAPIView, PlaceCreateAPIView, PlaceUpdateAPIView
from place import views
from funding.views import FundingLike, ViewExample
from review.views import ReviewLike
router = routers.DefaultRouter()
router.register('funding', FundingViewSet, basename='funding')
router.register('place',PlaceViewSet,basename='place')
router.register('review', ReviewListViewSet)
router.register('main-funding', MainFundingViewSet, basename='main_funding')
router.register('funding-comment', FundingCommentViewSet, basename='funding_comment')

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
    path('place_like/<str:user>/<str:q>/', views.PlaceLike),
    path('review_like/<str:user>/<int:id>/', ReviewLike),
    path('funding_like/<str:user>/<int:id>/', FundingLike),
    path('main-funding/', ViewExample.as_view()),
    url('api/main-funding/(?P<id>[\w-]+)/edit/$', MainFundingUpdateAPIView.as_view(), name='main_funding_update'),
    url('api/main-funding/(?P<id>[\w-]+)/delete/$', MainFundingDeleteAPIView.as_view(), name='main_funding_delete'),
    url('api/funding-comment/(?P<id>[\w-]+)/edit/$', FundingCommentUpdateAPIView.as_view(), name='funding_comment_update'),
    url('api/funding-comment/(?P<id>[\w-]+)/delete/$', FundingCommentDeleteAPIView.as_view(), name='funding_comment_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


