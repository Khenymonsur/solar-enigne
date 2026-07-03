from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Manufacturer
from django.db.models import Avg


from .forms import SolarPanelForm
from .models import SolarPanel



class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "equipment/manufacturers/manufacturer_list.html"
    context_object_name = "manufacturers"
    paginate_by = 15

    queryset = Manufacturer.objects.order_by("name")


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
        return reverse_lazy("equipment:manufacturers")


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
        return reverse_lazy("equipment:manufacturers")


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer

    template_name = "equipment/manufacturers/manufacturer_confirm_delete.html"

    success_url = reverse_lazy("equipment:manufacturers")




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