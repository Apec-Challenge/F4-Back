from django.contrib import admin
from .models import Place, GooglePlace, PPE

class PPEAdmin(admin.ModelAdmin):
    model = PPE

class PlaceAdmin(admin.ModelAdmin):
    model = Place

class GooglePlaceAdmin(admin.ModelAdmin):
    model = GooglePlace

admin.site.register(PPE,PPEAdmin)
admin.site.register(Place,PlaceAdmin)
admin.site.register(GooglePlace,GooglePlace)