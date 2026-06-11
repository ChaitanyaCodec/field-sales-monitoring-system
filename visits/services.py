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

    # Check whether employee already has an active visit
    active_visit = Visit.objects.filter(
        employee=employee,
        status="CHECKED_IN"
    ).exists()

    if active_visit:
        raise ValueError(
            "Employee already has an active visit."
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

# Complete an active customer visit
def check_out_customer(
    visit_id,
    latitude,
    longitude,
    notes=""
):
    """
    Complete a customer visit.

    Business Rules:
    - Visit must exist.
    - Visit must be CHECKED_IN.
    - Save checkout details.
    - Mark visit as COMPLETED.
    """

    # Find active visit
    visit = Visit.objects.filter(
        id=visit_id,
        status="CHECKED_IN"
    ).first()

    if not visit:
        raise ValueError(
            "Active visit not found."
        )

    # Save checkout details
    visit.checkout_time = timezone.now()
    visit.checkout_latitude = latitude
    visit.checkout_longitude = longitude

    visit.notes = notes
    visit.status = "COMPLETED"

    # Save updated fields
    visit.save(
        update_fields=[
            "checkout_time",
            "checkout_latitude",
            "checkout_longitude",
            "notes",
            "status",
        ]
    )

    return visit