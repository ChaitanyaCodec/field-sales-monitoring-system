from django.utils import timezone

from attendance.models import Attendance
from customers.models import Customer
from .models import Visit


def check_in_customer(
    employee,
    customer_id,
    latitude,
    longitude
):
    """
    Create a customer visit.

    Business Rules:
    - Employee must have ACTIVE attendance.
    - Customer must exist.
    - Visit status starts as CHECKED_IN.
    """

    # Find today's active attendance
    attendance = Attendance.objects.filter(
        employee=employee,
        status="ACTIVE"
    ).first()

    if not attendance:
        raise ValueError(
            "Employee has not started work."
        )

    # Get customer
    customer = Customer.objects.get(
        id=customer_id
    )

    # Create visit record
    visit = Visit.objects.create(
        employee=employee,
        attendance=attendance,
        customer=customer,

        checkin_time=timezone.now(),

        checkin_latitude=latitude,
        checkin_longitude=longitude,

        status="CHECKED_IN"
    )

    return visit

from django.utils import timezone

from attendance.models import Attendance
from customers.models import Customer
from .models import Visit


def check_in_customer(
    employee,
    customer_id,
    latitude,
    longitude
):
    """
    Create a customer visit.

    Business Rules:
    - Employee must have ACTIVE attendance.
    - Customer must exist.
    - Visit status starts as CHECKED_IN.
    """

    # Find today's active attendance
    attendance = Attendance.objects.filter(
        employee=employee,
        status="ACTIVE"
    ).first()

    if not attendance:
        raise ValueError(
            "Employee has not started work."
        )

    # Get customer
    customer = Customer.objects.get(
        id=customer_id
    )

    # Create visit record
    visit = Visit.objects.create(
        employee=employee,
        attendance=attendance,
        customer=customer,

        checkin_time=timezone.now(),

        checkin_latitude=latitude,
        checkin_longitude=longitude,

        status="CHECKED_IN"
    )

    return visit