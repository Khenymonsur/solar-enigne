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
            return {
                "found": False,
                "item": None,
                "quantity": 0,
                "required": Decimal(required_watts),
                "installed": Decimal("0"),
                "reserve": Decimal("0"),
                "status": "NOT_FOUND",
                "message": "No active solar panel found.",
            }

        quantity = math.ceil(
            Decimal(required_watts)
            / Decimal(panel.wattage)
        )

        installed = Decimal(quantity) * Decimal(panel.wattage)

        reserve = installed - Decimal(required_watts)

        return {
            "found": True,
            "item": panel,
            "quantity": quantity,
            "required": Decimal(required_watts),
            "installed": installed,
            "reserve": reserve,
            "status": "OK",
            "message": None,
        }



    def get_battery(self, voltage, required_ah):

        battery = (
            Battery.objects
            .filter(
                active=True,
                voltage=voltage,
            )
            .order_by("-capacity_ah")
            .first()
        )

        if battery is None:
            return {

                "found": False,
                "item": None,
                "quantity": 0,
                "required": Decimal(required_ah),
                "installed": Decimal("0"),
                "reserve": Decimal("0"),
                "status": "NOT_FOUND",
                "message": f"No active {voltage}V battery found.",

            }

        quantity = math.ceil(
            Decimal(required_ah)
            / Decimal(battery.capacity_ah)
        )

        installed = (
                Decimal(quantity)
                * Decimal(battery.capacity_ah)
        )

        reserve = installed - Decimal(required_ah)

        return {

            "found": True,
            "item": battery,
            "quantity": quantity,
            "required": Decimal(required_ah),
            "installed": installed,
            "reserve": reserve,
            "status": "OK",
            "message": None,

        }



    def get_inverter(self, required_watts):

        required_kva = (
            Decimal(required_watts) * Decimal("1.25")
        ) / Decimal("1000")

        inverter = (
            Inverter.objects
            .filter(active=True)
            .order_by("-capacity_kva")
            .first()
        )

        if inverter is None:
            return {
                "found": False,
                "item": None,
                "quantity": 0,
                "required": required_kva,
                "installed": Decimal("0"),
                "reserve": Decimal("0"),
                "status": "NOT_FOUND",
                "message": "No active inverter found.",
            }

        installed = Decimal(inverter.capacity_kva)
        reserve = installed - required_kva

        status = (
            "OK"
            if installed >= required_kva
            else "UNDERSIZED"
        )

        message = None

        if status == "UNDERSIZED":
            message = (
                f"Required: {required_kva:.2f} kVA. "
                f"Largest available: {installed:.2f} kVA."
            )

        return {
            "found": True,
            "item": inverter,
            "quantity": 1,
            "required": required_kva,
            "installed": installed,
            "reserve": reserve,
            "status": status,
            "message": message,
        }




    def get_controller(self, voltage, current):

        controller = (
            ChargeController.objects
            .filter(
                active=True,
                voltage=voltage,
            )
            .order_by("-current_rating")
            .first()
        )

        if controller is None:
            return {
                "found": False,
                "item": None,
                "quantity": 0,
                "required": Decimal(current),
                "installed": Decimal("0"),
                "reserve": Decimal("0"),
                "status": "NOT_FOUND",
                "message": f"No active {voltage}V controller found.",
            }

        installed = Decimal(controller.current_rating)
        reserve = installed - Decimal(current)

        status = (
            "OK"
            if installed >= Decimal(current)
            else "UNDERSIZED"
        )

        message = None

        if status == "UNDERSIZED":
            message = (
                f"Required: {Decimal(current):.0f}A. "
                f"Largest available: {installed:.0f}A."
            )

        return {
            "found": True,
            "item": controller,
            "quantity": 1,
            "required": Decimal(current),
            "installed": installed,
            "reserve": reserve,
            "status": status,
            "message": message,
        }