from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def clean_nickname(self, nickname):
        return nickname
    def save_user(self, request, user, form, commit=True):
            """
            Saves a new `User` instance using information provided in the
            signup form.
            """
            from allauth.account.utils import user_email, user_field, user_username
            data = form.cleaned_data
            email = data.get("email")
            username = data.get("username")
            nickname = data.get("nickname")
            user_email(user, email)
            user_username(user, username)
            user_field(user, "nickname", nickname)
            if "password1" in data:
                user.set_password(data["password1"])
            else:
                user.set_unusable_password()
            self.populate_username(request, user)
            if commit:
                # Ability not to commit makes it easier to derive from
                # this adapter by adding
                user.save()
            return user

# class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

            