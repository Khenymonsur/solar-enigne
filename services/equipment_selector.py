from decimal import Decimal

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

        battery = (
            Battery.objects
            .filter(
                active=True,
                voltage=voltage,
                capacity_ah__gte=required_ah,
            )
            .order_by("capacity_ah")
            .first()
        )

        if battery:
            return {
                "found": True,
                "item": battery,
                "required": required_ah,
                "message": None,
            }

        return {
            "found": False,
            "item": None,
            "required": required_ah,
            "message": (
                f"No active {voltage}V battery "
                f"≥ {required_ah:.0f}Ah found."
            ),
        }




    def get_inverter(self, required_watts):

        required_kva = (
                               Decimal(required_watts)
                               * Decimal("1.25")
                       ) / Decimal("1000")

        inverter = (
            Inverter.objects
            .filter(
                active=True,
                capacity_kva__gte=required_kva,
            )
            .order_by("capacity_kva")
            .first()
        )

        if inverter:
            return {
                "found": True,
                "item": inverter,
                "required": required_kva,
                "message": None,
            }

        return {
            "found": False,
            "item": None,
            "required": required_kva,
            "message": (
                f"No active inverter "
                f"≥ {required_kva:.2f} kVA found."
            ),
        }




    def get_controller(self, voltage, current):

        controller = (
            ChargeController.objects
            .filter(
                active=True,
                voltage=voltage,
                current_rating__gte=current,
            )
            .order_by("current_rating")
            .first()
        )

        if controller:
            return {
                "found": True,
                "item": controller,
                "required": current,
                "message": None,
            }

        return {
            "found": False,
            "item": None,
            "required": current,
            "message": (
                f"No active {voltage}V controller "
                f"≥ {current}A found."
            ),
        }