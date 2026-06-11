from django.utils import timezone

from attendance.models import Attendance
from customers.models import Customer

from .models import Visit
from .utils import calculate_distance


def check_in_customer(
    employee,
    customer_id,
    latitude,
    longitude
):
    """
    Create a customer visit after GPS verification.

    Business Rules:
    - Employee must have ACTIVE attendance.
    - Customer must exist.
    - Employee must be within 100 meters
      of customer location.
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

    # Calculate distance between
    # employee location and customer location
    distance = calculate_distance(
        latitude,
        longitude,
        customer.latitude,
        customer.longitude
    )

    # Allow check-in only if employee
    # is within 100 meters
    if distance > 100:
        raise ValueError(
            f"Check-in denied. Employee is "
            f"{round(distance, 2)} meters away."
        )

    # Create visit
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