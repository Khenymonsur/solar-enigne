from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from customers.models import Customer
from audits.models import Assessment
from equipment.models import (
    Battery,
    Inverter,
    SolarPanel,
    ChargeController,
)

from django.utils import timezone


@login_required(login_url="accounts:login")
def dashboard(request):

    equipment_count = (
        Battery.objects.count()
        + Inverter.objects.count()
        + SolarPanel.objects.count()
        + ChargeController.objects.count()
    )

    context = {
        "customer_count": Customer.objects.count(),
        "assessment_count": Assessment.objects.count(),
        "equipment_count": equipment_count,
        "report_count": 0,
        "recent_assessments": Assessment.objects.order_by("-created_at")[:10],
        "now": timezone.now(),
    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )