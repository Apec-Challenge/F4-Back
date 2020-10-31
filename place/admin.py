from django.contrib import admin
from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    model = Place
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': '__all__'}
        ),
    )
    filter_horizontal = ("user_likes",)

admin.site.register(Place,PlaceAdmin)
