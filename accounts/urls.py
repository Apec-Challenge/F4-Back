from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('rest-auth/login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('rest-auth/registration/', views.CustomRegisterView.as_view(), name='custom_registration'),
    path('api/accounts/money-recharge/', views.MoneyRechargeViewSet.as_view(), name='money_recharge'),
    path('api/accounts/fund-place/', views.FundToPlace.as_view(), name='fund_to_place')
]