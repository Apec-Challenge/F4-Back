from django.contrib import admin
from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    model = Place


admin.site.register(Place,PlaceAdmin)
