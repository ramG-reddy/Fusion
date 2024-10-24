from applications.globals.models import HoldsDesignation


def get_designation(userid):
    user_designation = HoldsDesignation.objects.select_related(
        "user", "working", "designation"
    ).filter(user=userid)
    return user_designation
