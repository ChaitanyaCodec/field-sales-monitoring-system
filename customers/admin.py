from django.contrib import admin
from .models import Customer
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "customer_code",
        "name",
        "phone",
        "is_active",
    )

    search_fields = (
        "customer_code",
        "name",
        "phone",
    )

    list_filter = (
        "is_active",
    )