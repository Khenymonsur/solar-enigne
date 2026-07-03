from decimal import Decimal


class LoadCalculator:
    """
    Core engineering calculations.

    Every recommendation in the system
    starts from this class.
    """

    def __init__(self, assessment):
        self.assessment = assessment

    @property
    def appliances(self):
        return self.assessment.appliances.all()

    def connected_load(self):
        """
        Total running load (Watts)
        """

        return sum(
            appliance.quantity * appliance.power_rating
            for appliance in self.appliances
        )

    def surge_load(self):
        """
        Total starting load
        """

        return sum(
            appliance.quantity * appliance.surge_power
            for appliance in self.appliances
        )

    def critical_load(self):
        """
        Total critical appliances
        """

        return sum(
            appliance.quantity * appliance.power_rating
            for appliance in self.appliances.filter(
                critical_load=True
            )
        )

    def daily_energy(self):
        """
        Watt-hours per day
        """

        return sum(
            appliance.quantity
            * appliance.power_rating
            * appliance.hours_per_day
            for appliance in self.appliances
        )

    def total_appliances(self):
        return self.appliances.count()