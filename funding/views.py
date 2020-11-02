from requests import Response
from django.http import HttpResponse
from .models import Funding
from accounts.models import User
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from django_filters import FilterSet, CharFilter
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework.viewsets import ModelViewSet
from .serializers import FundingSerializer, FundingPutSerializer, FundingDateSerializer
from django.db.models import Count, F, Q


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


class FundingKeywordFilter(FilterSet):
    class Meta:
        model = Funding
        fields = {
            'id': ['exact']
        }




class FundingViewSet(ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
    # filterset_class = FundingFilter
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'created_at', 'title', 'description', 'content_text', 'ended_at')
    http_method_names = ['get', 'post']
    filterset_class = FundingKeywordFilter
    lookup_field = 'like_count'

    def get_queryset(self):
        orderbyList = ['-created_at']
        q = self.request.GET.get('q', '')
        key = self.request.GET.get('key','')

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
        elif q == "keyword":
            search = (Funding.objects.order_by('created_at').filter(Q (title__icontains=key) | Q (content_text__icontains=key) | Q (description__icontains=key)))
            return search
        else:
            return Funding.objects.all().order_by(*orderbyList)


def FundingLike(request, user, id):
    if request.method == 'GET':
        print(user, id)
        place = Funding.objects.get(id=id)
        print(place.user_likes.all().values('nickname'))
        user_id = User.objects.get(nickname=user)
        print(user_id)
        if place.user_likes.filter(nickname=user).exists():
            place.user_likes.remove(user_id)
            print("좋아요 취소")
        else:
            place.user_likes.add(user_id)
            print("좋아요")
    return HttpResponse(status=200)