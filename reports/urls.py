from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [

    path(
        "",
        views.ReportListView.as_view(),
        name="list",
    ),

    path(
        "<int:pk>/",
        views.ReportDetailView.as_view(),
        name="detail",
    ),

    path(
        "<int:pk>/pdf/",
        views.ReportPDFView.as_view(),
        name="pdf",
    ),

]