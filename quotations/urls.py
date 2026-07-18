from django.urls import path

from .views import (
    QuotationListView,
    QuotationDetailView,
    QuotationCreateView,
    QuotationUpdateView,
    QuotationDeleteView,
    GenerateQuotationView,
)

from .pdf import quotation_pdf

app_name = "quotations"

urlpatterns = [

    path(
        "",
        QuotationListView.as_view(),
        name="list",
    ),

    path(
        "new/",
        QuotationCreateView.as_view(),
        name="create",
    ),

    path(
        "<int:pk>/",
        QuotationDetailView.as_view(),
        name="detail",
    ),

    path(
        "<int:pk>/edit/",
        QuotationUpdateView.as_view(),
        name="update",
    ),

    path(
        "<int:pk>/delete/",
        QuotationDeleteView.as_view(),
        name="delete",
    ),

    path(
        "<int:assessment_id>/generate/",
        GenerateQuotationView.as_view(),
        name="generate",
    ),

    path(
        "<int:pk>/pdf/",
        quotation_pdf,
        name="pdf",
),

]