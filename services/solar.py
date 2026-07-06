from decimal import Decimal
import math


class SolarCalculator:

    def __init__(
        self,
        daily_energy,
        peak_sun_hours=Decimal("5.50"),
        panel_size=Decimal("550"),
    ):
        self.energy = Decimal(daily_energy)
        self.psh = Decimal(peak_sun_hours)
        self.panel = Decimal(panel_size)

    def required_watts(self):
        return self.energy / self.psh

    def number_of_panels(self):
        return math.ceil(
            self.required_watts() / self.panel
        )