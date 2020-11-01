from .models import Place
from django.http import HttpResponse


def PlaceLike(request, user, q):

    if request.method == 'GET':
        print(user, q)
        place = Place.objects.get(place_id=q)
        print(place.user_likes.all().values('nickname'))
        if place.user_likes.filter(nickname=user).exists():
            place.user_likes.remove(user)
            print("좋아요 취소")
        else:
            place.user_likes.add(user)
            print("좋아요")
    return HttpResponse(status=200)