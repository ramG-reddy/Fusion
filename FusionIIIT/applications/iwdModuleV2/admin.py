from django.contrib import admin

from .models import (
    Addendum,
    AESDetails,
    Agreement,
    CorrigendumTable,
    ExtensionOfTimeDetails,
    FinancialBidDetails,
    FinancialContractorDetails,
    LetterOfIntentDetails,
    Milestones,
    NoOfTechnicalBidTimes,
    PageOneDetails,
    PageThreeDetails,
    PageTwoDetails,
    PreBidDetails,
    Projects,
    TechnicalBidContractorDetails,
    TechnicalBidDetails,
    WorkOrderForm,
)

# Register your models here.
admin.site.register(Projects)
admin.site.register(PageOneDetails)
admin.site.register(AESDetails)
admin.site.register(PageTwoDetails)
admin.site.register(CorrigendumTable)
admin.site.register(Addendum)
admin.site.register(PreBidDetails)
admin.site.register(TechnicalBidDetails)
admin.site.register(TechnicalBidContractorDetails)
admin.site.register(FinancialBidDetails)
admin.site.register(FinancialContractorDetails)
admin.site.register(LetterOfIntentDetails)
admin.site.register(WorkOrderForm)
admin.site.register(Agreement)
admin.site.register(Milestones)
admin.site.register(PageThreeDetails)
admin.site.register(ExtensionOfTimeDetails)
admin.site.register(NoOfTechnicalBidTimes)
