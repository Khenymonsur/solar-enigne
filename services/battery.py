from decimal import Decimal


class BatteryCalculator:

    def __init__(
        self,
        load,
        backup_hours,
        voltage=48,
        dod=Decimal("0.80"),
    ):

        self.load = Decimal(load)

        self.hours = Decimal(backup_hours)

        self.voltage = Decimal(voltage)

        self.dod = Decimal(dod)

    def required_wh(self):
        """
        Required energy in Watt-hours.
        """
        return self.load * self.hours

    def required_ah(self):
        """
        Required battery capacity in Amp-hours.
        """
        return (
            self.required_wh()
            /
            (self.voltage * self.dod)
        )

    @property
    def required_kwh(self):
        """
        Required energy in kWh.
        """
        return self.required_wh() / Decimal("1000")