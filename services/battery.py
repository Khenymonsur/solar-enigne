from decimal import Decimal


class BatteryCalculator:
    """
    Calculates the required battery bank capacity.

    Input:
        daily_energy (Wh/day)
        backup_hours
        system_voltage
        depth_of_discharge
    """

    def __init__(
        self,
        load,
        backup_hours,
        voltage=48,
        dod=Decimal("0.80"),
    ):

        self.daily_energy = Decimal(load)
        self.backup_hours = Decimal(backup_hours)
        self.voltage = Decimal(voltage)
        self.dod = Decimal(dod)

    @property
    def average_hourly_energy(self):
        """
        Average energy consumed every hour.
        """
        return self.daily_energy / Decimal("24")

    def required_wh(self):
        """
        Energy required during the backup period.
        """
        return (
            self.average_hourly_energy
            * self.backup_hours
        )

    def required_ah(self):
        """
        Required battery capacity.
        """
        return (
            self.required_wh()
            /
            (self.voltage * self.dod)
        )

    @property
    def required_kwh(self):
        """
        Required backup energy.
        """
        return self.required_wh() / Decimal("1000")