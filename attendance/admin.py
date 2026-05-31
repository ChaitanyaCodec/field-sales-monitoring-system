from django.contrib import admin
from .models import Attendance
# Register your models here.
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "date",
        "start_time",
        "end_time",
    )