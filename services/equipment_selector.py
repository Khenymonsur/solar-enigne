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

        required_watts = Decimal(required_watts)

        panels = (
            SolarPanel.objects
            .filter(active=True)
            .order_by("wattage")
        )

        if not panels.exists():
            return {
                "found": False,
                "item": None,
                "quantity": 0,
                "required": required_watts,
                "installed": Decimal("0"),
                "reserve": Decimal("0"),
                "status": "NOT_FOUND",
                "message": "No active solar panel found.",
            }

        best = None

        for panel in panels:

            quantity = math.ceil(
                required_watts / Decimal(panel.wattage)
            )

            installed = Decimal(quantity) * Decimal(panel.wattage)

            reserve = installed - required_watts

            total_cost = Decimal(quantity) * Decimal(panel.price)

            candidate = {
                "found": True,
                "item": panel,
                "quantity": quantity,
                "required": required_watts,
                "installed": installed,
                "reserve": reserve,
                "total_cost": total_cost,
                "status": "OK",
                "message": None,
            }

            if best is None:
                best = candidate
                continue

            if candidate["total_cost"] < best["total_cost"]:
                best = candidate
                continue

            if (
                    candidate["total_cost"] == best["total_cost"]
                    and candidate["reserve"] < best["reserve"]
            ):
                best = candidate

        return best



    def get_battery(self, voltage, required_ah):

        print("Voltage:", voltage)
        print("Required AH:", required_ah)

        batteries = Battery.objects.filter(
            active=True,
            voltage=voltage,
        )

        print("Batteries:", list(batteries))

        battery = batteries.order_by("-capacity_ah").first()

        print("Selected:", battery)

        required_ah = Decimal(required_ah)


        required_ah = Decimal(required_ah)

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
                "required": required_ah,
                "installed": Decimal("0"),
                "reserve": Decimal("0"),
                "status": "NOT_FOUND",
                "message": f"No active {voltage}V battery found.",
            }

        quantity = math.ceil(
            required_ah / Decimal(battery.capacity_ah)
        )

        installed = (
                Decimal(quantity)
                * Decimal(battery.capacity_ah)
        )

        reserve = installed - required_ah

        return {
            "found": True,
            "item": battery,
            "quantity": quantity,
            "required": required_ah,
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
            Inverter.objects.filter(
                active=True,
                capacity_kva__gte=required_kva,
            ).order_by("capacity_kva").first()
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



    def get_controller(self, voltage, required_current):

        required_current = Decimal(required_current)

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
                "required": required_current,
                "installed": Decimal("0"),
                "reserve": Decimal("0"),
                "status": "NOT_FOUND",
                "message": f"No active {voltage}V controller found.",
            }

        quantity = math.ceil(
            required_current / Decimal(controller.current_rating)
        )

        installed = (
                Decimal(quantity)
                * Decimal(controller.current_rating)
        )

        reserve = installed - required_current

        return {
            "found": True,
            "item": controller,
            "quantity": quantity,
            "required": required_current,
            "installed": installed,
            "reserve": reserve,
            "status": "OK",
            "message": None,
        }