from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model for Admins and Sales Employees.
    """

    ADMIN = "ADMIN"
    EMPLOYEE = "EMPLOYEE"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (EMPLOYEE, "Employee"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=EMPLOYEE,
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )

    employee_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )

    designation = models.CharField(
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return self.username