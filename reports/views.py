from django.shortcuts import render

# Import Visit model
from visits.models import Visit


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