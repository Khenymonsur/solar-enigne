import math


class ControllerCalculator:
    """
    Calculates the recommended solar charge controller
    current rating based on the solar array size.
    """

    def __init__(self, solar_watts, voltage=48):
        self.solar_watts = solar_watts
        self.voltage = voltage

    def current(self):
        """
        Returns the minimum controller current (Amps).
        """
        from decimal import Decimal

        return math.ceil(
            Decimal(self.solar_watts)
            / Decimal(self.voltage)
        )

    def recommended_controller(self):
        """
        Returns the next standard controller size.
        """
        standard_sizes = [20, 30, 40, 60, 80, 100, 120, 150]

        current = self.current()

        for size in standard_sizes:
            if current <= size:
                return size

        return current