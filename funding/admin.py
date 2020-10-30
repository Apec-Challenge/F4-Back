from django.contrib import admin
from .models import Funding

class FundingAdmin(admin.ModelAdmin):
    model = Funding
    filter_horizontal = ("user",)

admin.site.register(Funding, FundingAdmin)