from django.db import models


    # ===============================
    # MANUFACTURER CLASS
    # ===============================

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


    # ===============================
    # INVERTER CLASS
    # ===============================

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


    # ===============================
    # BATTERY CLASS
    # ===============================

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


    # ===============================
    # SOLAR PANEL CLASS
    # ===============================

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


    # ===============================
    # CHARGE CONTROLLER CLASS
    # ===============================

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

    # ===============================
    # APPLIANCE LIBRARY
    # ===============================

from django.db import models


class ApplianceCategory(models.TextChoices):
    LIGHTING = "Lighting", "Lighting"
    COOLING = "Cooling", "Cooling"
    KITCHEN = "Kitchen", "Kitchen"
    ENTERTAINMENT = "Entertainment", "Entertainment"
    OFFICE = "Office", "Office"
    INDUSTRIAL = "Industrial", "Industrial"
    AGRICULTURE = "Agriculture", "Agriculture"
    MEDICAL = "Medical", "Medical"
    OTHER = "Other", "Other"


class Appliance(models.Model):
    category = models.CharField(
        max_length=30,
        choices=ApplianceCategory.choices,
        default=ApplianceCategory.OTHER,
    )

    name = models.CharField(max_length=120)

    default_wattage = models.PositiveIntegerField()

    surge_factor = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=1.00,
    )

    default_hours = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=8,
    )

    energy_efficient = models.BooleanField(default=False)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return f"{self.name} ({self.default_wattage}W)"
