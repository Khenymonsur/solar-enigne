from decimal import Decimal
from customer_portal.services.session import AssessmentSessionService


class CustomerEstimationService:
    """
    Generates a preliminary estimate for customers.

    This is NOT the engineering recommendation engine.
    It provides an indicative system size based on
    customer-entered appliance data.
    """

    def __init__(self, request):

        self.request = request

        self.appliances = (
            AssessmentSessionService.selected_appliances(
                request
            )
        )

    # ------------------------------------
    # Connected Load
    # ------------------------------------

    def connected_load(self):

        total = Decimal("0")

        for appliance in self.appliances:

            total += Decimal(str(appliance["total"]))

        return round(total, 2)

    # ------------------------------------
    # Daily Energy
    # ------------------------------------

    def daily_energy(self):

        total = Decimal("0")

        for appliance in self.appliances:

            total += Decimal(
                str(appliance["daily_energy"])
            )

        return round(total, 2)

    # ------------------------------------
    # INVERTER RECOMMENDATION
    # ------------------------------------

    def recommended_inverter(self):

        kva = (
                      self.connected_load()
                      * Decimal("1.25")
              ) / Decimal("1000")

        return round(kva, 1)

    # ------------------------------------
    # BATTERY STORAGE
    # ------------------------------------

    def recommended_battery(self):

        backup_hours = (
            AssessmentSessionService.get(
                self.request
            )
            .get("power", {})
            .get("backup_hours", 8)
        )

        energy = (
                         self.connected_load()
                         * Decimal(str(backup_hours))
                 ) / Decimal("1000")

        return round(energy, 1)

    # ------------------------------------
    # SOLAR CAPACITY
    # ------------------------------------

    def recommended_solar(self):

        daily = self.daily_energy()

        peak_sun_hours = Decimal("5")

        solar = (
                        daily / peak_sun_hours
                ) * Decimal("1.2")

        return round(solar, 1)

    # ------------------------------------
    # BUDGET RANGE
    # ------------------------------------

    def estimated_budget(self):

        solar_kw = self.recommended_solar()

        low = solar_kw * Decimal("850000")

        high = solar_kw * Decimal("1000000")

        return {
            "low": round(low),
            "high": round(high),
        }

    # ------------------------------------
    # SUMMARY
    # ------------------------------------

    def summary(self):

        return {

            "connected_load": self.connected_load(),

            "daily_energy": self.daily_energy(),

            "recommended_inverter":
                self.recommended_inverter(),

            "recommended_battery":
                self.recommended_battery(),

            "recommended_solar":
                self.recommended_solar(),

            "budget":
                self.estimated_budget(),

        }