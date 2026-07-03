from django.db import models


class Manufacturer(models.Model):
    """
    Equipment manufacturer.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    logo = models.ImageField(
        upload_to="manufacturers/",
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True,
    )

    support_email = models.EmailField(blank=True)

    support_phone = models.CharField(
        max_length=30,
        blank=True
    )

    country = models.CharField(
        max_length=100,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name



class Inverter(models.Model):

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )

    model = models.CharField(max_length=100)

    capacity_kva = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    hybrid = models.BooleanField(default=True)

    voltage = models.PositiveIntegerField()

    efficiency = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    warranty = models.PositiveIntegerField(
        default=5,
    )

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"



class Battery(models.Model):

    TYPES = (
        ("Lithium", "Lithium"),
        ("Tubular", "Tubular"),
        ("Gel", "Gel"),
        ("AGM", "AGM"),
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )

    model = models.CharField(max_length=100)

    battery_type = models.CharField(
        max_length=20,
        choices=TYPES,
    )

    voltage = models.PositiveIntegerField()

    capacity_ah = models.PositiveIntegerField()

    cycle_life = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"




class SolarPanel(models.Model):

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )

    model = models.CharField(max_length=100)

    wattage = models.PositiveIntegerField()

    efficiency = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    warranty = models.PositiveIntegerField(
        default=25,
    )

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"



class ChargeController(models.Model):

    TYPES = (
        ("MPPT", "MPPT"),
        ("PWM", "PWM"),
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )

    model = models.CharField(max_length=100)

    controller_type = models.CharField(
        max_length=20,
        choices=TYPES,
    )

    current_rating = models.PositiveIntegerField()

    voltage = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"