from equipment.models import Appliance


class SessionAppliance:

    """
    Behaves like AssessmentAppliance.
    """

    def __init__(
        self,
        appliance,
        quantity,
    ):

        self.appliance = appliance

        self.quantity = quantity

        # Fields already expected by the engineering engine
        self.power_rating = appliance.power_rating
        self.surge_power = appliance.surge_power
        self.hours_per_day = appliance.hours_per_day
        self.critical_load = appliance.critical_load



class SessionApplianceManager:

    def __init__(self, appliances):

        self._appliances = appliances

    def all(self):

        return self._appliances

    def count(self):

        return len(self._appliances)




class SessionAssessment:

    """
    Adapter that behaves like the Assessment model.
    """

    def __init__(self, session_data):

        customer = session_data.get("customer", {})
        property_info = session_data.get("property", {})
        power = session_data.get("power", {})

        self.customer = customer

        self.property = property_info

        self.system_voltage = power.get(
            "system_voltage",
            48,
        )

        self.backup_hours = power.get(
            "backup_hours",
            8,
        )

        self.grid_available = (
            power.get("grid_available") == "yes"
        )

        self.generator_available = (
            power.get("generator_available") == "yes"
        )

        self.power_scope = power.get(
            "power_scope"
        )

        appliances = []

        for item in session_data.get(
            "appliances",
            [],
        ):

            try:
                appliance = Appliance.objects.get(
                    pk=item["appliance_id"]
                )
            except Appliance.DoesNotExist:
                continue

            appliances.append(

                SessionAppliance(
                    appliance,
                    item["quantity"],
                )

            )

        self.appliances = (

            SessionApplianceManager(
                appliances
            )

        )