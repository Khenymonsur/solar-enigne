from decimal import Decimal


from services.battery import BatteryCalculator
from services.calculations import LoadCalculator
from services.controller import ControllerCalculator
from services.equipment_selector import EquipmentSelector
from services.solar import SolarCalculator


class RecommendationEngine:

    def __init__(self, assessment):
        self.assessment = assessment
        self.load = LoadCalculator(assessment)

    def recommend(self):

        # =====================================================
        # ASSESSMENT INPUTS
        # =====================================================

        connected_load = self.load.connected_load()

        connected_load_kw = (
                connected_load / Decimal("1000")
        )

        # Returns Wh
        daily_energy_wh = self.load.daily_energy()

        # Convert to kWh for display
        daily_energy = daily_energy_wh / Decimal("1000")

        voltage = self.assessment.system_voltage
        backup = self.assessment.backup_hours
        sun_hours = self.assessment.peak_sun_hours

        # =====================================================
        # ENGINEERING CALCULATIONS
        # =====================================================

        battery_calc = BatteryCalculator(
            load=daily_energy_wh,
            backup_hours=backup,
            voltage=voltage,
        )

        battery_ah = battery_calc.required_ah()

        panel_calc = SolarCalculator(
            daily_energy=daily_energy_wh,
            peak_sun_hours=sun_hours,
        )

        solar_required = panel_calc.required_watts()

        controller_calc = ControllerCalculator(
            solar_required,
            voltage,
        )

        controller_current = controller_calc.current()

        required_inverter_kva = (
            connected_load * Decimal("1.25")
        ) / Decimal("1000")

        # =====================================================
        # EQUIPMENT SELECTION
        # =====================================================

        selector = EquipmentSelector()

        panel = selector.get_panel(solar_required)

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

        # =====================================================
        # SOLAR ARRAY
        # =====================================================

        panel_excess_capacity = Decimal("0")

        if panel["found"]:
            panel_excess_capacity = panel["reserve"]

        # =====================================================
        # INVERTER
        # =====================================================

        inverter_reserve_kva = inverter["reserve"]

        # =====================================================
        # CONTROLLER
        # =====================================================

        controller_spare_current = controller["reserve"]

        # =====================================================
        # DESIGN READINESS
        # =====================================================

        completed = sum([
            panel["status"] == "OK",
            battery["status"] == "OK",
            inverter["status"] == "OK",
            controller["status"] == "OK",
        ])

        design_progress = completed * 25
        design_ready = completed == 4

        # =====================================================
        # ENGINEERING NOTES
        # =====================================================

        solar_note = None

        if panel["found"]:
            solar_note = (
                f"{panel['quantity']} × "
                f"{panel['item'].wattage}W panels provide "
                f"{panel['installed']:.0f}W installed capacity."
            )

        battery_note = None

        if battery["found"]:
            battery_note = (
                f"{battery['quantity']} × "
                f"{battery['item'].capacity_ah}Ah batteries provide "
                f"{battery['installed']:.0f}Ah total capacity."
            )

        inverter_note = inverter["message"]

        if inverter["status"] == "OK":
            inverter_note = (
                f"{inverter['installed']:.2f} kVA inverter "
                f"meets the design requirement."
            )

        controller_note = controller["message"]

        if controller["status"] == "OK":
            controller_note = (
                f"{controller['installed']:.0f}A controller "
                f"meets the design requirement."
            )

        # =====================================================
        # RETURN RESULTS
        # =====================================================

        return {

            # =====================================================
            # DESIGN CALCULATIONS
            # =====================================================

            "connected_load": connected_load,
            "connected_load_kw": connected_load_kw,
            "daily_energy": daily_energy,
            "required_solar": solar_required,
            "required_battery_ah": battery_ah,
            "required_controller_current": controller_current,
            "required_inverter_kva": required_inverter_kva,

            # =====================================================
            # EQUIPMENT SELECTION
            # =====================================================

            "panel": panel["item"],
            "panel_quantity": panel["quantity"],
            "panel_capacity": panel["installed"],

            "panel_required": panel["required"],
            "panel_installed": panel["installed"],
            "panel_status": panel["status"],
            "panel_reserve": panel["reserve"],

            "battery": battery["item"],
            "battery_required": battery["required"],
            "battery_message": battery["message"],
            "battery_status": battery["status"],
            "battery_installed": battery["installed"],
            "battery_reserve": battery["reserve"],




            "inverter": inverter["item"],
            "inverter_required": inverter["required"],
            "inverter_message": inverter["message"],

            "controller": controller["item"],
            "controller_required": controller["required"],
            "controller_message": controller["message"],

            "inverter_quantity": inverter["quantity"],
            "inverter_installed": inverter["installed"],
            "inverter_status": inverter["status"],
            "inverter_reserve": inverter["reserve"],

            "controller_quantity": controller["quantity"],
            "controller_installed": controller["installed"],
            "controller_status": controller["status"],
            "controller_reserve": controller["reserve"],

            # =====================================================
            # ENGINEERING VALUES
            # =====================================================

            "panel_excess_capacity": panel_excess_capacity,
            "battery_quantity": battery["quantity"],
            "battery_installed_capacity": battery["installed"],
            "battery_reserve_capacity": battery["reserve"],
            "inverter_reserve_kva": inverter_reserve_kva,
            "controller_spare_current": controller_spare_current,

            # =====================================================
            # STATUS
            # =====================================================

            "design_progress": design_progress,
            "design_ready": design_ready,

            # =====================================================
            # NOTES
            # =====================================================

            "solar_note": solar_note,
            "battery_note": battery_note,
            "inverter_note": inverter_note,
            "controller_note": controller_note,

        }