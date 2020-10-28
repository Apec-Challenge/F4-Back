from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review


admin.site.register(Review, ReviewAdmin)
