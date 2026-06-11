from django.db import models
from django.conf import settings

from customers.models import Customer
from attendance.models import Attendance



class Visit(models.Model):
    """
    Stores customer visit details.
    """

    STATUS_CHOICES = [
        ("CHECKED_IN", "Checked In"),
        ("COMPLETED", "Completed"),
    ]

    # Employee who performed the visit
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="visits"
    )

    

    # Attendance record for that day
    attendance = models.ForeignKey(
        Attendance,
        on_delete=models.CASCADE,
        related_name="visits"
    )

    # Customer being visited
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="visits"
    )

    # Check-in information
    checkin_time = models.DateTimeField()

    checkin_latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )

    checkin_longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )

    # Check-out information
    checkout_time = models.DateTimeField(
        null=True,
        blank=True
    )

    checkout_latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    checkout_longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    # Meeting notes
    notes = models.TextField(
        blank=True
    )

    # Visit evidence photo
    photo = models.ImageField(
        upload_to="visit_photos/",
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="CHECKED_IN"
    )
    
    @property
    def duration_minutes(self):
        """
        Calculate visit duration in minutes.
        """

        if not self.checkout_time:
            return None

        duration = (
            self.checkout_time -
            self.checkin_time
        )

        return round(
            duration.total_seconds() / 60,
            2
        )
    class Meta:
        ordering = ["-checkin_time"]  #This ensures the newest visits appear first in the admin panel.

    def __str__(self):
        return f"{self.employee.username} - {self.customer.name}"