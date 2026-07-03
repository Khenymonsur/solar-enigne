class BatteryCalculator:

    def __init__(
        self,
        load,
        backup_hours,
        voltage=48,
        dod=0.8,
    ):

        self.load = load
        self.hours = backup_hours
        self.voltage = voltage
        self.dod = dod

    def required_wh(self):

        return self.load * self.hours

    def required_ah(self):

        return (
            self.required_wh()
            /
            (self.voltage * self.dod)
        )