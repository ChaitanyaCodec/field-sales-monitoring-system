from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_code} - {self.name}"