from django.contrib import admin
from .models import Funding, MainFunding, FundingComment

class FundingAdmin(admin.ModelAdmin):
    model = Funding
    filter_horizontal = ("backed_list",)

admin.site.register(Funding, FundingAdmin)


class MainFundingAdmin(admin.ModelAdmin):
    model = MainFunding
    filter_horizontal = ("main_funding",)

admin.site.register(MainFunding, MainFundingAdmin)


class FundingCommentAdmin(admin.ModelAdmin):
    model = FundingComment

admin.site.register(FundingComment, FundingCommentAdmin)