from django.db.models import Count
from django.db.models import Q

from .models import Appliance
from .forms import ApplianceForm


from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


from django.db.models import Avg


from .forms import (
    SolarPanelForm,
    BatteryForm,
    InverterForm,
    ChargeControllerForm,
)

from .models import (
    Manufacturer,
    SolarPanel,
    Battery,
    Inverter,
    ChargeController,
)



class ManufacturerListView(ListView):

    model = Manufacturer

    template_name = "equipment/manufacturers/manufacturer_list.html"

    context_object_name = "manufacturers"

    paginate_by = 15

    queryset = Manufacturer.objects.order_by("name")

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        queryset = Manufacturer.objects.all()

        context["manufacturers_count"] = queryset.count()

        context["countries_count"] = (
            queryset.exclude(country="")
            .values("country")
            .distinct()
            .count()
        )

        context["products_count"] = (
            SolarPanel.objects.count()
            + Battery.objects.count()
            + Inverter.objects.count()
            + ChargeController.objects.count()
        )

        context["active_products"] = (
            SolarPanel.objects.filter(active=True).count()
            + Battery.objects.filter(active=True).count()
            + Inverter.objects.filter(active=True).count()
            + ChargeController.objects.filter(active=True).count()
        )

        return context




class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = "equipment/manufacturers/manufacturer_detail.html"


class ManufacturerCreateView(CreateView):
    model = Manufacturer

    fields = "__all__"

    template_name = "equipment/manufacturers/manufacturer_form.html"

    def form_valid(self, form):

        messages.success(
            self.request,
            "Manufacturer created successfully."
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("equipment:manufacturers-list")


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer

    fields = "__all__"

    template_name = "equipment/manufacturers/manufacturer_form.html"

    def form_valid(self, form):

        messages.success(
            self.request,
            "Manufacturer updated successfully."
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("equipment:manufacturers-list")



class ManufacturerDeleteView(DeleteView):
    model = Manufacturer

    template_name = "equipment/manufacturers/manufacturer_confirm_delete.html"

    success_url = reverse_lazy("equipment:manufacturers-list")




class SolarPanelListView(ListView):

    model = SolarPanel

    template_name = "equipment/solar/panel_list.html"

    context_object_name = "panels"

    paginate_by = 15

    queryset = (
        SolarPanel.objects
        .select_related("manufacturer")
        .order_by("manufacturer__name", "model")
    )


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["manufacturers_count"] = Manufacturer.objects.count()

        context["active_count"] = SolarPanel.objects.filter(
            active=True
        ).count()

        context["average_wattage"] = (
                SolarPanel.objects.aggregate(
                    Avg("wattage")
                )["wattage__avg"] or 0
        )

        return context


class SolarPanelCreateView(CreateView):

    model = SolarPanel

    form_class = SolarPanelForm

    template_name = "equipment/solar/panel_form.html"

    success_url = reverse_lazy("equipment:panel-list")

    def form_valid(self, form):

        messages.success(
            self.request,
            "Solar panel added successfully."
        )

        return super().form_valid(form)



class SolarPanelUpdateView(UpdateView):

    model = SolarPanel

    form_class = SolarPanelForm

    template_name = "equipment/solar/panel_form.html"

    success_url = reverse_lazy("equipment:panel-list")

    def form_valid(self, form):

        messages.success(
            self.request,
            "Solar panel updated successfully."
        )

        return super().form_valid(form)



class SolarPanelDeleteView(DeleteView):

    model = SolarPanel

    template_name = "equipment/solar/panel_confirm_delete.html"

    success_url = reverse_lazy("equipment:panel-list")




class BatteryListView(ListView):

    model = Battery

    template_name = "equipment/batteries/battery_list.html"

    context_object_name = "batteries"

    paginate_by = 15

    queryset = (
        Battery.objects
        .select_related("manufacturer")
        .order_by("manufacturer__name", "model")
    )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["manufacturers_count"] = Manufacturer.objects.count()

        context["active_count"] = Battery.objects.filter(
            active=True
        ).count()

        return context


class BatteryDetailView(DetailView):

    model = Battery

    template_name = "equipment/batteries/battery_detail.html"


class BatteryCreateView(CreateView):

    model = Battery

    form_class = BatteryForm

    template_name = "equipment/batteries/battery_form.html"

    success_url = reverse_lazy("equipment:battery-list")

    def form_valid(self, form):

        messages.success(
            self.request,
            "Battery added successfully."
        )

        return super().form_valid(form)


class BatteryUpdateView(UpdateView):

    model = Battery

    form_class = BatteryForm

    template_name = "equipment/batteries/battery_form.html"

    success_url = reverse_lazy("equipment:battery-list")

    def form_valid(self, form):

        messages.success(
            self.request,
            "Battery updated successfully."
        )

        return super().form_valid(form)


class BatteryDeleteView(DeleteView):

    model = Battery

    template_name = "equipment/batteries/battery_confirm_delete.html"

    success_url = reverse_lazy("equipment:battery-list")




class InverterListView(ListView):

    model = Inverter

    template_name = "equipment/inverters/inverter_list.html"

    context_object_name = "inverters"

    paginate_by = 15

    queryset = (
        Inverter.objects
        .select_related("manufacturer")
        .order_by("manufacturer__name", "capacity_kva")
    )


class InverterDetailView(DetailView):

    model = Inverter

    template_name = "equipment/inverters/inverter_detail.html"


class InverterCreateView(CreateView):

    model = Inverter

    form_class = InverterForm

    template_name = "equipment/inverters/inverter_form.html"

    success_url = reverse_lazy("equipment:inverter-list")

    def form_valid(self, form):

        messages.success(
            self.request,
            "Inverter added successfully."
        )

        return super().form_valid(form)


class InverterUpdateView(UpdateView):

    model = Inverter

    form_class = InverterForm

    template_name = "equipment/inverters/inverter_form.html"

    success_url = reverse_lazy("equipment:inverter-list")

    def form_valid(self, form):

        messages.success(
            self.request,
            "Inverter updated successfully."
        )

        return super().form_valid(form)


class InverterDeleteView(DeleteView):

    model = Inverter

    template_name = "equipment/inverters/inverter_confirm_delete.html"

    success_url = reverse_lazy("equipment:inverter-list")




class ChargeControllerListView(ListView):

    model = ChargeController

    template_name = "equipment/controllers/controller_list.html"

    context_object_name = "controllers"

    paginate_by = 15

    queryset = (
        ChargeController.objects
        .select_related("manufacturer")
        .order_by(
            "manufacturer__name",
            "current_rating",
        )
    )


class ChargeControllerDetailView(DetailView):

    model = ChargeController

    template_name = "equipment/controllers/controller_detail.html"


class ChargeControllerCreateView(CreateView):

    model = ChargeController

    form_class = ChargeControllerForm

    template_name = "equipment/controllers/controller_form.html"

    success_url = reverse_lazy("equipment:controller-list")

    def form_valid(self, form):

        messages.success(
            self.request,
            "Charge Controller added successfully."
        )

        return super().form_valid(form)


class ChargeControllerUpdateView(UpdateView):

    model = ChargeController

    form_class = ChargeControllerForm

    template_name = "equipment/controllers/controller_form.html"

    success_url = reverse_lazy("equipment:controller-list")

    def form_valid(self, form):

        messages.success(
            self.request,
            "Charge Controller updated successfully."
        )

        return super().form_valid(form)


class ChargeControllerDeleteView(DeleteView):

    model = ChargeController

    template_name = (
        "equipment/controllers/controller_confirm_delete.html"
    )

    success_url = reverse_lazy("equipment:controller-list")





class ApplianceListView(ListView):
    model = Appliance
    template_name = "equipment/appliances/appliance_list.html"
    context_object_name = "appliances"
    paginate_by = 15

    def get_queryset(self):
        queryset = Appliance.objects.order_by("category", "name")

        q = self.request.GET.get("q")

        if q:
            queryset = queryset.filter(
                Q(name__icontains=q)
                | Q(category__icontains=q)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = Appliance.objects.all()

        context["active_count"] = queryset.filter(active=True).count()

        context["categories_count"] = (
            queryset.values("category")
            .distinct()
            .count()
        )

        context["average_wattage"] = (
            queryset.aggregate(
                Avg("default_wattage")
            )["default_wattage__avg"]
            or 0
        )

        return context


class ApplianceDetailView(DetailView):
    model = Appliance
    template_name = "equipment/appliances/appliance_detail.html"



class ApplianceCreateView(CreateView):
    model = Appliance
    form_class = ApplianceForm
    template_name = "equipment/appliances/appliance_form.html"
    success_url = reverse_lazy("equipment:appliance-list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Appliance created successfully."
        )
        return super().form_valid(form)



class ApplianceUpdateView(UpdateView):
    model = Appliance
    form_class = ApplianceForm
    template_name = "equipment/appliances/appliance_form.html"
    success_url = reverse_lazy("equipment:appliance-list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Appliance updated successfully."
        )
        return super().form_valid(form)



class ApplianceDeleteView(DeleteView):
    model = Appliance
    template_name = (
        "equipment/appliances/appliance_confirm_delete.html"
    )
    success_url = reverse_lazy("equipment:appliance-list")

    def delete(self, request, *args, **kwargs):
        messages.success(
            request,
            "Appliance deleted successfully."
        )
        return super().delete(request, *args, **kwargs)