import math


class SolarCalculator:

    def __init__(
        self,
        daily_energy,
        peak_sun_hours=5.5,
        panel_size=550,
    ):

        self.energy = daily_energy

        self.psh = peak_sun_hours

        self.panel = panel_size

    def required_watts(self):

        return self.energy / self.psh

    def number_of_panels(self):

        return math.ceil(
            self.required_watts()
            /
            self.panel
        )
