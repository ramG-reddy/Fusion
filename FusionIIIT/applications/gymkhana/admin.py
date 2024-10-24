from django.contrib import admin

from .models import (
    Club_budget,
    Club_info,
    Club_member,
    Club_report,
    Core_team,
    Event_info,
    Fest_budget,
    Form_available,
    Inventory,
    Other_report,
    Registration_form,
    Session_info,
    Voting_choices,
    Voting_polls,
    Voting_voters,
)

# Register your models here.


class ClubInfoAdmin(admin.ModelAdmin):
    raw_id_fields = ("co_ordinator", "co_coordinator")


class ClubMemberAdmin(admin.ModelAdmin):
    raw_id_fields = ("member",)


admin.site.register(Club_info, ClubInfoAdmin)
admin.site.register(Club_member, ClubMemberAdmin)
admin.site.register(Core_team)
admin.site.register(Club_budget)
admin.site.register(Session_info)
admin.site.register(Event_info)
admin.site.register(Club_report)
admin.site.register(Fest_budget)
admin.site.register(Other_report)
admin.site.register(Voting_polls)
admin.site.register(Voting_choices)
admin.site.register(Voting_voters)
admin.site.register(Registration_form)
admin.site.register(Form_available)
admin.site.register(Inventory)
