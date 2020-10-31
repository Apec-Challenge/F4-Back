from django.shortcuts import render, redirect
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from allauth.socialaccount.providers.github.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)
from .serializers import CustomRegisterSeriializer
from rest_framework import viewsets
from .models import User
from django.conf import settings
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.google.provider import GoogleProvider
import requests

BASE_URL = 'http://127.0.0.1:8000/'

# from google.oauth2 import id_token
# from google.auth.transport import requests as google_requests

# class GoogleOAuth2AdapterIdToken(GoogleOAuth2Adapter):
#     def complete_login(self, request, app, token, **kwargs):
#         idinfo = id_token.verify_oauth2_token(token.token, google_requests.Request(), app.client_id)
#         if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
#             raise ValueError('Wrong issuer.')
#         extra_data = idinfo
#         login = self.get_provider() \
#                 .sociallogin_from_response(request, extra_data)
#         return login

# oauth2_login = OAuth2LoginView.adapter_view(GoogleOAuth2AdapterIdToken)
# oauth2_callback = OAuth2CallbackView.adapter_view(GoogleOAuth2AdapterIdToken)

class GoogleDualAdapter(GoogleOAuth2Adapter):
    tokeninfo_url = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
    def complete_login(self, request, app, token, **kwargs):
        provider = self.get_provider()
        if provider.id_token_mode:
            resp = requests.get(
                self.tokeninfo_url,
                params={'id_token': token.token}
            )
        else:
            resp = requests.get(
                self.profile_url,
                params={
                    'access_token': token.token,
                    'alt': 'json'
                }
            )
        resp.raise_for_status()
        extra_data = resp.json()
        return provider.sociallogin_from_response(
            request, extra_data
        )





class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = BASE_URL + 'rest-auth/google/callback/'


class CustomLoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        mydata = {"pk" : self.user.pk, "email": self.user.email, "nickname": self.user.nickname}
        response.data.update(mydata)
        return response

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSeriializer


def google_login(request):
    client_id = getattr(settings, 'GOOGLE_CLIENT_ID')
    redirect_uri = BASE_URL + "rest-auth/google/callback/"
    return redirect(
        f"https://accounts.google.com/o/oauth2/auth?scope=https%3A//www.googleapis.com/auth/drive.metadata.readonly&access_type=offline&include_granted_scopes=true&response_type=code&state=state_parameter_passthrough_value&redirect_uri={redirect_uri}&client_id={client_id}"
        )

def google_callback(request):
    redirect_uri = BASE_URL + "rest-auth/google/callback/"
    client_id = getattr(settings, 'GOOGLE_CLIENT_ID')
    client_secret = getattr(settings, 'GOOGLE_SECRET_KEY')
    code = request.GET.get('code')
    # print(code)
    token = requests.post(f"https://oauth2.googleapis.com/token?code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&grant_type=authorization_code")
    token_json = token.json()
    print(token_json)
    access_token = token_json.get("access_token")
    print(access_token)
    print(11111111111)
    print(code)
    # profile = requests.get(f"https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={access_token}")
    # profile = requests.get(f"https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization" : f"Bearer {access_token}"})
    # data = {'access_token' : access_token, 'code' : code}
    # a = requests.post(f"{BASE_URL}rest-auth/google/login/", data=data)
    # print(a)


def kakao_login(request):
    rest_api_key =  getattr(settings, 'KAKAO_REST_API_KEY')
    redirect_uri = BASE_URL + "rest-auth/kakao/callbak/"
    print(redirect_uri)
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


def kakao_callback(request):
    try:
        rest_api_key =  getattr(settings, 'KAKAO_REST_API_KEY')
        print(rest_api_key)
        redirect_uri = BASE_URL + "accounts/kakao/login/callback/" ##callback
        code = request.GET.get("code") ## code
        token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}")
        token_request_json = token_request.json()
        print(token_request_json)
    #     error = token_request_json.get("error")
    #     # # print(error)
    #     if error is not None:
    #         raise KaKaoException()
    #     access_token = token_request_json.get("access_token")
    #     profile_request = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"})
    #     profile_json = profile_request.json()
    #     properties = profile_json.get('properties')
    #     kakao_account = profile_json.get('kakao_account')
    #     print(kakao_account)
    #     email = kakao_account.get("email", None)
    #     if email is None:
    #         raise KaKaoException()
    #     profile = kakao_account.get("profile")
    #     nickanme = profile.get("nickname")
    #     print(access_token)
    #     print(111111111)
    #     print(code)
        

    #     try:
    #         user_in_db = User.objects.get(email=email)
    #         if user_in_db is None:
    #             raise KaKaoException()
    #         else:
    #             data = {'access_token' : access_token, 'code' : code}
    #             accept = requests.post(
    #                 f"{BASE_URL}accounts/kakao/login/todjango/", data=data
    #             )
    #             print(accept)
    #             # accept_jwt = accept_json.get("token")

    #             User.objects.filter(email=email).update(
    #                                                     is_active=True,
    #             )
    #             # login(request, user_in_db, backend="django.contrib.auth.backends.ModelBackend",)
    #     except User.DoesNotExist:
    #         data = {'access_token' : access_token, 'code' : code}
    #         accept = requests.post(
    #             f"{BASE_URL}accounts/kakao/login/todjango/", data=data
    #         )
    #         print(accept.json)
    #         # accept_json = accept.json()
    #         # new_user_in_db = User.objects.create(
    #         #     email=email,
    #         #     # nickname=nickname,
    #         #     user_type='1',
    #         #     is_active=True,
    #         # )
    #         # new_user_in_db.set_unusable_password()
    #         # new_user_in_db.save()
    #         # login(
    #         #     request,
    #         #     new_user_in_db,
    #         #     backend="django.contrib.auth.backends.ModelBackend",
    #         # )
    #         # accept_jwt = accept_json.get("token")
            
    #     return redirect("/signin/")
    #     # profile_image_url = profile.get('thumbnail_image_url')
    #     # a = requests.post("http://" + domain + "accounts/kakao/login/todjango/", data={'access_token' : access_token, 'code' : code})
    #     # print(a.status_code)
    #     # a_error = a_json.get('error')
    #     # print(a_error)
    except KaKaoException:
        return redirect('/signin/')


from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    client_id = OAuth2Client