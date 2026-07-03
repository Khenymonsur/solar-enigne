from django.urls import path

from . import views

app_name = "equipment"

urlpatterns = [

    path(
        "manufacturers/",
        views.ManufacturerListView.as_view(),
        name="manufacturers",
    ),

    path(
        "manufacturers/add/",
        views.ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),

    path(
        "manufacturers/<int:pk>/",
        views.ManufacturerDetailView.as_view(),
        name="manufacturer-detail",
    ),

    path(
        "manufacturers/<int:pk>/edit/",
        views.ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),

    path(
        "manufacturers/<int:pk>/delete/",
        views.ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),


    path(
        "solar-panels/",
        views.SolarPanelListView.as_view(),
        name="panel-list",
    ),

    path(
        "solar-panels/add/",
        views.SolarPanelCreateView.as_view(),
        name="panel-create",
    ),

    path(
        "solar-panels/<int:pk>/edit/",
        views.SolarPanelUpdateView.as_view(),
        name="panel-update",
    ),

    path(
        "solar-panels/<int:pk>/delete/",
        views.SolarPanelDeleteView.as_view(),
        name="panel-delete",
    ),

]