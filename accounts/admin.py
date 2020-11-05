from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'nickname')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'place_likes', 'review_likes', 'funding_likes', 'nickname','money')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'place_likes', 'review_likes', 'funding_likes', 'nickname', 'money')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ("place_likes", 'review_likes', 'funding_likes')


admin.site.register(User, CustomUserAdmin)