from django.contrib import admin
from .models import Appliance


@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "default_wattage",
        "default_hours",
        "energy_efficient",
        "active",
    )

    list_filter = (
        "category",
        "energy_efficient",
        "active",
    )

    search_fields = (
        "name",
        "category",
    )
