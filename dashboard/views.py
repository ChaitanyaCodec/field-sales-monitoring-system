from django.shortcuts import render
from django.utils import timezone

from accounts.models import User
from customers.models import Customer
from attendance.models import Attendance
from visits.models import Visit


def dashboard_view(request):
    """
    Display summary statistics for the sales monitoring system.
    """

    # Get today's date
    today = timezone.localdate()

    context = {

        # Total employees
        "total_employees": User.objects.filter(
            role="EMPLOYEE"
        ).count(),

        # Total customers
        "total_customers": Customer.objects.count(),

        # Today's attendance records
        "today_attendance": Attendance.objects.filter(
            date=today
        ).count(),

        # Total visits today
        "today_visits": Visit.objects.filter(
            checkin_time__date=today
        ).count(),

        # Completed visits
        "completed_visits": Visit.objects.filter(
            status="COMPLETED"
        ).count(),

        "recent_visits": Visit.objects.select_related(
            "employee",
            "customer"
        ).order_by(
            "-checkin_time"
        )[:5],        
        
        # Recent attendance records
        "recent_attendance": Attendance.objects.select_related(
            "employee"
        ).order_by(
            "-date",
            "-start_time"
        )[:5],
    }
    

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )

    