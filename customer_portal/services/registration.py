from django.db import transaction

from customers.models import Customer
from audits.models import Assessment, Appliance

from customer_portal.services import AssessmentSessionService


class RegistrationService:
    """
    Converts a completed Customer Portal assessment
    into permanent database records.
    """

    @classmethod
    @transaction.atomic
    def complete_registration(cls, request, user):
        """
        Creates:
            - Customer
            - Assessment
            - Assessment Appliances

        Returns:
            Assessment instance
        """

        session = AssessmentSessionService.get(request)

        customer_data = session.get("customer", {})
        property_data = session.get("property", {})
        power_data = session.get("power", {})
        appliances = session.get("appliances", [])

        # ----------------------------------------
        # Customer
        # ----------------------------------------

        customer, created = Customer.objects.update_or_create(

            user=user,

            defaults={

                "full_name": customer_data["full_name"],

                "phone": customer_data["phone"],

                "whatsapp": customer_data.get(
                    "whatsapp",
                    "",
                ),

                "address": property_data["address"],

                "state": property_data["state"],

                "lga": property_data.get(
                    "lga",
                    "",
                ),

                "building_type": property_data.get(
                    "building_type",
                    Customer.RESIDENTIAL,
                ),

            },

        )

        # ----------------------------------------
        # Assessment
        # ----------------------------------------

        assessment = Assessment.objects.create(

            customer=customer,

            project_name="Customer Portal Assessment",

            backup_hours=power_data.get(
                "backup_hours",
                8,
            ),

            notes="Submitted from Customer Portal.",

            status="Completed",

        )

        # ----------------------------------------
        # Appliances
        # ----------------------------------------

        for item in appliances:

            Appliance.objects.create(

                assessment=assessment,

                appliance_name=item["name"],

                quantity=item["quantity"],

                power_rating=item["watts"],

                hours_per_day=item["hours_per_day"],

            )

        # ----------------------------------------
        # Clear Session
        # ----------------------------------------

        AssessmentSessionService.clear(request)

        return assessment