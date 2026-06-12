from django.urls import path

# Import report view
from .views import visit_report

urlpatterns = [

    # Visit report page
    path(
        "",
        visit_report,
        name="visit_report"
    ),
]