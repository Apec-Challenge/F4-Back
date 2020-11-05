from django.shortcuts import render, redirect
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSeriializer, MoneyRechargeSerializer, UserSerializer
from rest_framework import viewsets
from .models import User
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from funding.models import Funding
from place.models import Place
from django_filters.rest_framework import DjangoFilterBackend, filters

BASE_URL = 'http://127.0.0.1:8000/'


class CustomLoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        mydata = {"pk" : self.user.pk, "email": self.user.email, "nickname": self.user.nickname}
        response.data.update(mydata)
        return response


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSeriializer


class MoneyRechargeViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = MoneyRechargeSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        user = queryset.get(pk=self.request.user.pk)
        return user

    def get(self, request):
        return JsonResponse({'money' : request.user.money}, status=status.HTTP_200_OK)

    def put(self, request):
        add_money = request.data.get('money')
        current_money = request.user.money
        now_money = int(add_money) + current_money
        request.data['money'] = now_money
        
        return self.update(request)


class FundToPlace(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        place_id = request.data.get('place_id')
        funding_place = Funding.objects.get(place=Place.objects.get(place_id=place_id))
        current_money_funding = funding_place.funding_amount
        current_money = request.user.money
        money = funding_place.funding_price
        add_money = int(money)
        user_id = request.user.pk

        if current_money < add_money:
            raise ValueError("You don't have enough Money. Please Try again after charging")
        try:
            User.objects.filter(pk=user_id).update(money=current_money - int(add_money))
            Funding.objects.filter(place_id=place_id).update(funding_amount=current_money_funding + add_money)
            # data = {'now_money' : request.user.money - add_money, 'now_amount' : funding_place.funding_amount + add_money, 'goal' : funding_place.funding_goal_amount}
            funding_place.backed_list.add(user_id)
            return HttpResponse(status=200)
        except:
            return HttpResponse(data="The error occured. Please Try again", status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ['get', 'post']
    lookup_field = 'id'
