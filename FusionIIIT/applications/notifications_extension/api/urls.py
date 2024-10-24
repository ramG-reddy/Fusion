# urls.py
from django.urls import path

from .views import (
    AcademicsModuleNotificationAPIView,
    AssistantshipClaimNotificationAPIView,
    CentralMessNotificationAPIView,
    ComplaintSystemNotificationAPIView,
    Delete,
    DepartmentNotificationAPIView,
    FileTrackingNotificationAPIView,
    GymkhanaEventNotificationAPIView,
    GymkhanaSessionNotificationAPIView,
    GymkhanaVotingNotificationAPIView,
    HealthcareCenterNotificationAPIView,
    HostelModuleNotificationAPIView,
    LeaveModuleNotificationAPIView,
    MarkAsRead,
    NotificationsList,
    OfficeDeanPnDNotificationAPIView,
    OfficeDeanRSPCNotificationAPIView,
    OfficeDeanSNotificationAPIView,
    OfficeModuleNotificationAPIView,
    PlacementCellNotificationAPIView,
    ResearchProceduresNotificationAPIView,
    ScholarshipPortalNotificationAPIView,
    VisitorsHostelNotificationAPIView,
)

urlpatterns = [
    path("notifications/", NotificationsList.as_view(), name="notifications"),
    path("delete/", Delete.as_view(), name="delete"),
    path("mark_as_read/", MarkAsRead.as_view(), name="mark_as_read"),
    path(
        "leave_module_notification/",
        LeaveModuleNotificationAPIView.as_view(),
        name="leave_module_notification",
    ),
    path(
        "placement_cell_notification/",
        PlacementCellNotificationAPIView.as_view(),
        name="placement_cell_notification",
    ),
    path(
        "academics_module_notification/",
        AcademicsModuleNotificationAPIView.as_view(),
        name="academics_module_notification",
    ),
    path(
        "office_module_notification/",
        OfficeModuleNotificationAPIView.as_view(),
        name="office_module_notification",
    ),
    path(
        "central_mess_notification/",
        CentralMessNotificationAPIView.as_view(),
        name="central_mess_notification",
    ),
    path(
        "visitors_hostel_notification/",
        VisitorsHostelNotificationAPIView.as_view(),
        name="visitors_hostel_notification",
    ),
    path(
        "healthcare_center_notification/",
        HealthcareCenterNotificationAPIView.as_view(),
        name="healthcare_center_notification",
    ),
    path(
        "file_tracking_notification/",
        FileTrackingNotificationAPIView.as_view(),
        name="file_tracking_notification",
    ),
    path(
        "scholarship_portal_notification/",
        ScholarshipPortalNotificationAPIView.as_view(),
        name="scholarship_portal_notification",
    ),
    path(
        "complaint_system_notification/",
        ComplaintSystemNotificationAPIView.as_view(),
        name="complaint_system_notification",
    ),
    path(
        "office_dean_PnD_notification/",
        OfficeDeanPnDNotificationAPIView.as_view(),
        name="office_dean_PnD_notification",
    ),
    path(
        "office_dean_S_notification/",
        OfficeDeanSNotificationAPIView.as_view(),
        name="office_dean_S_notification",
    ),
    path(
        "gymkhana_voting/",
        GymkhanaVotingNotificationAPIView.as_view(),
        name="gymkhana_voting",
    ),
    path(
        "gymkhana_session/",
        GymkhanaSessionNotificationAPIView.as_view(),
        name="gymkhana_session",
    ),
    path(
        "gymkhana_event/",
        GymkhanaEventNotificationAPIView.as_view(),
        name="gymkhana_event",
    ),
    path(
        "assistantship_claim/",
        AssistantshipClaimNotificationAPIView.as_view(),
        name="assistantship_claim",
    ),
    path(
        "department_notification/",
        DepartmentNotificationAPIView.as_view(),
        name="department_notification",
    ),
    path(
        "office_dean_RSPC_notification/",
        OfficeDeanRSPCNotificationAPIView.as_view(),
        name="office_dean_RSPC_notification",
    ),
    path(
        "research_procedures_notification/",
        ResearchProceduresNotificationAPIView.as_view(),
        name="research_procedures_notification",
    ),
    path(
        "hostel_notifications/",
        HostelModuleNotificationAPIView.as_view(),
        name="hostel_notifications",
    ),
]
