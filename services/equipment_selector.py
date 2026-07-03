import math

from equipment.models import (
    Battery,
    ChargeController,
    Inverter,
    SolarPanel,
)


class EquipmentSelector:

    def get_panel(self, required_watts):

        panel = (
            SolarPanel.objects
            .filter(active=True)
            .order_by("-wattage")
            .first()
        )

        if panel is None:
            return None

        quantity = math.ceil(
            required_watts / panel.wattage
        )

        return {
            "panel": panel,
            "quantity": quantity,
            "capacity": quantity * panel.wattage,
        }

    def get_battery(self, voltage, required_ah):

        return (
            Battery.objects
            .filter(
                active=True,
                voltage=voltage,
                capacity_ah__gte=required_ah,
            )
            .order_by("capacity_ah")
            .first()
        )

    def get_inverter(self, required_watts):
        """
        Select the smallest inverter that can safely handle
        the required load.
        """

        required_kva = (required_watts * 1.25) / 1000

        return (
            Inverter.objects
            .filter(
                active=True,
                capacity_kva__gte=required_kva,
            )
            .order_by("capacity_kva")
            .first()
        )

    def get_controller(self, voltage, current):

        return (
            ChargeController.objects
            .filter(
                active=True,
                voltage=voltage,
                current_rating__gte=current,
            )
            .order_by("current_rating")
            .first()
        )