from .models import Review
from accounts.models import User
from django.http import HttpResponse


def ReviewLike(request, user, id):

    if request.method == 'GET':
        print(user, id)
        place = Review.objects.get(id=id)
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