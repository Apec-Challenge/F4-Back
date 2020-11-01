from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault('user_type', 'consumer')
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(unique=True, max_length=255)
    nickname = models.CharField(max_length=10, blank=False,unique=True)
    user_type = models.CharField(max_length=10, blank=False, null=True)
    money = models.PositiveIntegerField(blank=True, default=0)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    place_likes = models.ManyToManyField("place.Place", related_name='user_likes',blank=True)
    funding_likes = models.ManyToManyField("funding.Funding", related_name='user_likes',blank=True)
    review_likes = models.ManyToManyField("review.Review", related_name='user_likes',blank=True)

    objects = UserManager()

    def __str__(self):
        return self.nickname
