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

admin.site.register(Place,PlaceAdmin)
