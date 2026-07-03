from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import AssessmentForm
from .models import Assessment
from services.recommendation import RecommendationEngine


class AssessmentListView(ListView):
    model = Assessment
    template_name = "audits/assessment_list.html"
    context_object_name = "assessments"
    paginate_by = 10

    def get_queryset(self):
        queryset = (
            Assessment.objects
            .select_related("customer")
            .order_by("-created_at")
        )

        search = self.request.GET.get("q")

        if search:
            queryset = queryset.filter(
                Q(project_name__icontains=search)
                | Q(customer__full_name__icontains=search)
                | Q(customer__company_name__icontains=search)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        assessments = Assessment.objects.all()

        context["assessment_count"] = assessments.count()

        context["draft_count"] = assessments.filter(
            status="Draft"
        ).count()

        context["completed_count"] = assessments.filter(
            status="Completed"
        ).count()

        context["report_count"] = assessments.filter(
            report_generated=True
        ).count()

        return context


class AssessmentDetailView(DetailView):
    model = Assessment
    template_name = "audits/assessment_detail.html"
    context_object_name = "assessment"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        assessment = self.object

        recommendation = RecommendationEngine(
            assessment
        ).recommend()

        context["recommendation"] = recommendation

        context["appliances"] = (
            assessment.appliances.all()
        )

        context["total_appliances"] = (
            assessment.total_appliances
        )

        context["connected_load"] = (
            assessment.connected_load
        )

        context["daily_energy"] = (
            assessment.daily_energy
        )

        context["peak_load"] = (
            assessment.peak_load
        )

        context["critical_load"] = (
            assessment.total_critical_load
        )

        return context



class AssessmentCreateView(CreateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = "audits/assessment_form.html"

    def form_valid(self, form):

        messages.success(
            self.request,
            "Assessment created successfully."
        )

        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy(
            "audits:detail",
            kwargs={
                "pk": self.object.pk,
            },
        )


class AssessmentUpdateView(UpdateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = "audits/assessment_form.html"

    def form_valid(self, form):

        messages.success(
            self.request,
            "Assessment updated successfully."
        )

        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy(
            "audits:detail",
            kwargs={
                "pk": self.object.pk,
            },
        )


class AssessmentDeleteView(DeleteView):
    model = Assessment
    template_name = "audits/assessment_confirm_delete.html"
    success_url = reverse_lazy("audits:list")

    def delete(self, request, *args, **kwargs):

        messages.success(
            request,
            "Assessment deleted successfully."
        )

        return super().delete(request, *args, **kwargs)