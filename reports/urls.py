from django.urls import path

# Import report views
from .views import (
    visit_report,
    attendance_report
)

urlpatterns = [

    # Visit Report
    path(
        "",
        visit_report,
        name="visit_report"
    ),

    # Attendance Report
    path(
        "attendance/",
        attendance_report,
        name="attendance_report"
    ),
]