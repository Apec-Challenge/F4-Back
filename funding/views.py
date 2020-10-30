from requests import Response
from .models import Funding
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework.viewsets import ModelViewSet
from .serializers import FundingSerializer, FundingPutSerializer, FundingDateSerializer
# from rest_framework.filters import OrderingFilter



class FundingCreateViewSet(ListCreateAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    http_method_names = ['post']


class FundingUpdateAPIView(UpdateAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingPutSerializer
    lookup_field = 'id'


class FundingDeleteAPIView(DestroyAPIView):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    lookup_field = 'id'


# class FundingFilter(FilterSet):
#     class Meta:
#         model = Funding
#         fields = {
#
#
#         }


class FundingViewSet(ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    # filterset_class = FundingFilter
    # filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ['like_count', 'ended_at', 'created_at']
    http_method_names = ['get', 'post']
    lookup_field = 'like_count'

    def get_queryset(self):
        orderbyList = ['created_at']
        q = self.request.GET.get('q')

        if q == 'like_count':
            return Funding.objects.all().order_by('-like_count')
        elif q == "ended_at":
            return Funding.objects.all().order_by('ended_at')
        else:
            return Funding.objects.all().order_by(*orderbyList)



