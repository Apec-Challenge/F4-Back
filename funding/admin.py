from django.contrib import admin
from .models import Funding

class FundingAdmin(admin.ModelAdmin):
    model = Funding

admin.site.register(Funding, FundingAdmin)