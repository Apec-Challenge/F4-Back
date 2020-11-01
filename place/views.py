from .models import Place
from accounts.models import User
from django.http import HttpResponse


def PlaceLike(request, user, q):
    if request.method == 'GET':
        print(user, q)

        place = Place.objects.get(place_id=q)
        print(place.user_likes.all())
        print(place.user_likes.all().values('nickname'))
        user_id = User.objects.get(nickname=user)
        print(user_id)
        if user_id in place.user_likes.all():
            # place.user_likes.filter(nickname=user).exists():
            place.user_likes.remove(user_id)
            print("좋아요 취소")
        else:
            place.user_likes.add(user_id)
            print("좋아요")
    return HttpResponse(status=200)