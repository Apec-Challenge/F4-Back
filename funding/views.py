from requests import Response
from django.http import HttpResponse
from .models import Funding
from accounts.models import User
from .serializers import FundingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


class ViewExample(APIView):
    def get(self,request):
        fundinglist = Funding.objects.all()
        serializer = FundingSerializer(fundinglist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
