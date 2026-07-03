from django.urls import path

from .views import (
    AssessmentCreateView,
    AssessmentDetailView,
    AssessmentListView,
    AssessmentUpdateView,
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
]