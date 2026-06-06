from django.contrib import admin
from .models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """
    Configuration for Visit model in Django Admin.
    """

    # Columns displayed in admin list page
    list_display = (
        "employee",
        "customer",
        "checkin_time",
        "checkout_time",
        "status",
    )

    # Sidebar filters
    list_filter = (
        "status",
    )

    # Search functionality
    search_fields = (
        "employee__username",
        "customer__name",
    )