from django.urls import path

from .views import (
    AssessmentListView,
    AssessmentDetailView,
    AssessmentCreateView,
    AssessmentUpdateView,
    AssessmentDeleteView,
    ApplianceCreateView,
    ApplianceUpdateView,
    ApplianceDeleteView,
)

app_name = "audits"

urlpatterns = [

    path(
        "",
        AssessmentListView.as_view(),
        name="list",
    ),

    path(
        "new/<int:customer_id>/",
        AssessmentCreateView.as_view(),
        name="create",
    ),

    path(
        "<int:pk>/",
        AssessmentDetailView.as_view(),
        name="detail",
    ),

    path(
        "<int:pk>/edit/",
        AssessmentUpdateView.as_view(),
        name="update",
    ),

    path(
        "<int:pk>/delete/",
        AssessmentDeleteView.as_view(),
        name="delete",
    ),

    path(
        "<int:assessment_id>/appliances/add/",
        ApplianceCreateView,
        name="appliance-add",
    ),

    path(
        "appliances/<int:pk>/edit/",
        ApplianceUpdateView,
        name="appliance-update",
    ),

    path(
        "appliances/<int:pk>/delete/",
        ApplianceDeleteView,
        name="appliance-delete",
    ),

]