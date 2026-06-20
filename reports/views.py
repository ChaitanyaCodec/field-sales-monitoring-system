from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Import Visit model
from visits.models import Visit

# Import Attendance model
from attendance.models import Attendance
@login_required
def visit_report(request):
    """
    Visit Report

    Displays all customer visits with:
    - Employee
    - Customer
    - Check-In Time
    - Check-Out Time
    - Visit Status
    - Visit Duration
    """

    # Fetch visit records with related employee
    # and customer information.
    visits = Visit.objects.select_related(
        "employee",
        "customer"
    ).order_by(
        "-checkin_time"
    )

    return render(
        request,
        "reports/visit_report.html",
        {
            "visits": visits
        }
    )
@login_required
# Attendance Report View
def attendance_report(request):
    """
    Attendance Report

    Displays employee attendance records with:
    - Employee
    - Date
    - Start Time
    - End Time
    - Status
    """

    # Fetch attendance records along with
    # related employee information.
    attendance_records = Attendance.objects.select_related(
        "employee"
    ).order_by(
        "-date",
        "-start_time"
    )

    return render(
        request,
        "reports/attendance_report.html",
        {
            "attendance_records": attendance_records
        }
    )