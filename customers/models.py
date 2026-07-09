from django.db import models


class Customer(models.Model):
    RESIDENTIAL = "Residential"
    COMMERCIAL = "Commercial"
    INDUSTRIAL = "Industrial"

    BUILDING_TYPES = [
        (RESIDENTIAL, "Residential"),
        (COMMERCIAL, "Commercial"),
        (INDUSTRIAL, "Industrial"),
    ]

    full_name = models.CharField(max_length=200)
    company_name = models.CharField(
        max_length=200,
        blank=True,
    )

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    whatsapp = models.CharField(
        max_length=20,
        blank=True,
    )

    address = models.TextField()

    state = models.CharField(
        max_length=100
    )

    lga = models.CharField(
        max_length=100,
        blank=True
    )

    area = models.CharField(
        max_length=100,
        blank=True,
        help_text="Town, district or estate (e.g. Lekki Phase 1, GRA, Wuse II)"
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    building_type = models.CharField(
        max_length=20,
        choices=BUILDING_TYPES,
        default=RESIDENTIAL,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name