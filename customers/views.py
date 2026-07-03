from django.contrib import messages
from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"
    paginate_by = 20

    def get_queryset(self):
        queryset = Customer.objects.annotate(
            assessment_total=Count("assessments")
        )

        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(full_name__icontains=search)
                | Q(company_name__icontains=search)
                | Q(email__icontains=search)
                | Q(phone__icontains=search)
                | Q(state__icontains=search)
                | Q(city__icontains=search)
            )

        return queryset.order_by("full_name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["customer_count"] = Customer.objects.count()

        context["residential_count"] = Customer.objects.filter(
            building_type=Customer.RESIDENTIAL
        ).count()

        context["commercial_count"] = Customer.objects.filter(
            building_type=Customer.COMMERCIAL
        ).count()

        context["industrial_count"] = Customer.objects.filter(
            building_type=Customer.INDUSTRIAL
        ).count()

        return context


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"
    context_object_name = "object"


class CustomerCreateView(CreateView):
    model = Customer

    fields = [
        "full_name",
        "company_name",
        "email",
        "phone",
        "whatsapp",
        "address",
        "state",
        "city",
        "building_type",
    ]

    template_name = "customers/customer_form.html"

    success_url = reverse_lazy("customers:list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Customer created successfully.",
        )
        return super().form_valid(form)


class CustomerUpdateView(UpdateView):
    model = Customer

    fields = [
        "full_name",
        "company_name",
        "email",
        "phone",
        "whatsapp",
        "address",
        "state",
        "city",
        "building_type",
    ]

    template_name = "customers/customer_form.html"

    success_url = reverse_lazy("customers:list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Customer updated successfully.",
        )
        return super().form_valid(form)


class CustomerDeleteView(DeleteView):
    model = Customer

    template_name = "customers/customer_confirm_delete.html"

    success_url = reverse_lazy("customers:list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Customer deleted successfully.",
        )
        return super().form_valid(form)