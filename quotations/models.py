from datetime import timedelta
from decimal import Decimal

from django.db import models
from django.utils import timezone


class Quotation(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("sent", "Sent"),
        ("viewed", "Viewed"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("expired", "Expired"),
    ]

    quotation_no = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
    )

    assessment = models.OneToOneField(
        "audits.Assessment",
        on_delete=models.CASCADE,
        related_name="quotation",
    )

    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        related_name="quotations",
    )

    issue_date = models.DateField(auto_now_add=True)

    valid_until = models.DateField(
        blank=True,
        null=True,
    )

    subtotal = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    installation_cost = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    transport_cost = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    discount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    vat = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    grand_total = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Quotation"
        verbose_name_plural = "Quotations"

    def __str__(self):
        return self.quotation_no

    def save(self, *args, **kwargs):
        if not self.quotation_no:
            year = timezone.now().year
            last_id = Quotation.objects.count() + 1
            self.quotation_no = f"QT-{year}-{last_id:05d}"

        if not self.valid_until:
            self.valid_until = timezone.now().date() + timedelta(days=30)

        self.grand_total = (
            self.subtotal
            + self.installation_cost
            + self.transport_cost
            + self.vat
            - self.discount
        )

        super().save(*args, **kwargs)


class QuotationItem(models.Model):
    quotation = models.ForeignKey(
        Quotation,
        related_name="items",
        on_delete=models.CASCADE,
    )

    category = models.CharField(
        max_length=50)

    manufacturer = models.CharField(
        max_length=100)

    model = models.CharField(
        max_length=100)

    specification = models.CharField(
        max_length=150)

    description = models.CharField(
        max_length=255)

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    unit_price = models.DecimalField(
        max_digits=14,
        decimal_places=2,
    )

    total = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.description} ({self.quantity})"

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.unit_price
        super().save(*args, **kwargs)



