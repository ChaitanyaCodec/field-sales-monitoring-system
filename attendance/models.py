from django.db import models
from django.conf import settings


class Attendance(models.Model):
    """
    Stores daily attendance information for a sales employee.

    One employee can have only one attendance record per day.
    """

    # Attendance status choices
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),         # Employee is currently working
        ("COMPLETED", "Completed"),   # Employee has ended the workday
    ]

    # Employee associated with this attendance record
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="attendances"
    )

    # Attendance date
    date = models.DateField()

    # Workday start timestamp
    start_time = models.DateTimeField(
        null=True,
        blank=True
    )

    # Workday end timestamp
    end_time = models.DateTimeField(
        null=True,
        blank=True
    )

    # Current attendance status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    # GPS coordinates when employee starts work
    start_latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    start_longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    # GPS coordinates when employee ends work
    end_latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    end_longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    # Audit fields
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        # Prevent multiple attendance records
        # for the same employee on the same day
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "date"],
                name="unique_employee_attendance_per_day"
            )
        ]

        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.employee.username} - {self.date}"