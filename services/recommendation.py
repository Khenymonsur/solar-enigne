from decimal import Decimal

from services.calculations import LoadCalculator
from services.battery import BatteryCalculator
from services.controller import ControllerCalculator
from services.solar import SolarCalculator
from services.equipment_selector import EquipmentSelector


class RecommendationEngine:

    def __init__(self, assessment):

        self.assessment = assessment

        self.load = LoadCalculator(assessment)

    def recommend(self):

        connected_load = self.load.connected_load()

        daily_energy = self.load.daily_energy()

        voltage = self.assessment.system_voltage

        backup = self.assessment.backup_hours

        sun_hours = self.assessment.peak_sun_hours

        battery_calc = BatteryCalculator(
            load=daily_energy,
            backup_hours=backup,
            voltage=voltage,
        )

        battery_ah = battery_calc.required_ah()

        panel_calc = SolarCalculator(
            daily_energy=daily_energy,
            peak_sun_hours=sun_hours,
        )

        solar_required = panel_calc.required_watts()

        controller_calc = ControllerCalculator(
            solar_required,
            voltage,
        )

        controller_current = controller_calc.current()

        selector = EquipmentSelector()

        panel_data = selector.get_panel(solar_required)


        battery = selector.get_battery(
            voltage,
            battery_ah,
        )

        inverter = selector.get_inverter(
            connected_load,
        )

        controller = selector.get_controller(
            voltage,
            controller_current,
        )

        return {

            # =====================================================
            # ENGINEERING CALCULATIONS
            # =====================================================

            "connected_load": connected_load,
            "daily_energy": daily_energy,

            "required_solar": solar_required,
            "required_battery_ah": battery_ah,
            "required_controller_current": controller_current,

            "required_inverter_kva": (
                                             connected_load * Decimal("1.25")
                                     ) / Decimal("1000"),

            # =====================================================
            # SOLAR PANEL
            # =====================================================

            "panel": panel_data["panel"] if panel_data else None,
            "panel_quantity": panel_data["quantity"] if panel_data else 0,
            "panel_capacity": panel_data["capacity"] if panel_data else 0,

            # =====================================================
            # BATTERY
            # =====================================================

            "battery": battery["item"],
            "battery_required": battery["required"],
            "battery_message": battery["message"],

            # =====================================================
            # INVERTER
            # =====================================================

            "inverter": inverter["item"],
            "inverter_required": inverter["required"],
            "inverter_message": inverter["message"],

            # =====================================================
            # CONTROLLER
            # =====================================================

            "controller": controller["item"],
            "controller_required": controller["required"],
            "controller_message": controller["message"],

        }


