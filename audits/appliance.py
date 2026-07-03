from django.db import models
from .models import Assessment


class Appliance(models.Model):

    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,
        related_name="appliances",
    )

    appliance = models.CharField(
        max_length=200,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    power_rating = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    surge_power = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    hours_per_day = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    critical_load = models.BooleanField(
        default=False,
    )

    simultaneous = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.appliance