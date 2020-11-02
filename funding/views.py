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
from django.db.models import Count, F


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


class FundingViewSet(ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    # filterset_class = FundingFilter
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['ended_at', 'created_at', 'id']
    http_method_names = ['get', 'post']
    lookup_field = 'like_count'

    def get_queryset(self):
        orderbyList = ['created_at']
        q = self.request.GET.get('q')

        if q == 'like_count':
            return Funding.objects.annotate(like_count=Count('user_likes')).order_by('-like_count')
        elif q == "ended_at":
            return Funding.objects.all().order_by('ended_at')
        elif q == "deadline":
            return Funding.objects.all().order_by('ended_at')
        elif q == "hot":
            return Funding.objects.annotate(user_count=Count('backed_list'))\
                .order_by('-user_count')
        elif q == "achievement":
            return Funding.objects.annotate(achievement_rate=F('funding_amount')/F('funding_goal_amount')) \
                .order_by('-achievement_rate')
        else:
            return Funding.objects.all().order_by(*orderbyList)
