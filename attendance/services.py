from django.utils import timezone

from .models import Attendance


def start_work(employee, latitude=None, longitude=None):
    """
    Start an employee's workday.

    Business Rules:
    - Employee can start work only once per day.
    - Creates a new attendance record.
    - Attendance status is set to ACTIVE.
    """

    # Get current local date based on Django timezone settings
    today = timezone.localdate()

    # Check whether attendance already exists for today
    attendance_exists = Attendance.objects.filter(
        employee=employee,
        date=today
    ).exists()

    if attendance_exists:
        raise ValueError(
            "Attendance already started for today."
        )

    # Create attendance record
    attendance = Attendance.objects.create(
        employee=employee,
        date=today,
        start_time=timezone.now(),
        start_latitude=latitude,
        start_longitude=longitude,
        status="ACTIVE"
    )

    return attendance


def end_work(employee, latitude=None, longitude=None):
    """
    End an employee's workday.

    Business Rules:
    - Employee must have an ACTIVE attendance record.
    - End time and end location are recorded.
    - Attendance status is changed to COMPLETED.
    """

    # Get current local date
    today = timezone.localdate()

    # Find today's active attendance record
    attendance = Attendance.objects.filter(
        employee=employee,
        date=today,
        status="ACTIVE"
    ).first()

    if not attendance:
        raise ValueError(
            "No active attendance found."
        )

    # Record workday end information
    attendance.end_time = timezone.now()
    attendance.end_latitude = latitude
    attendance.end_longitude = longitude
    attendance.status = "COMPLETED"

    # Save only modified fields
    attendance.save(
        update_fields=[
            "end_time",
            "end_latitude",
            "end_longitude",
            "status",
        ]
    )

    return attendance