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

# ===============================
# SOLAR PANEL
# ===============================

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

# ===============================
# BATTERIES
# ===============================

    path(
        "batteries/",
        views.BatteryListView.as_view(),
        name="battery-list",
    ),

    path(
        "batteries/add/",
        views.BatteryCreateView.as_view(),
        name="battery-create",
    ),

    path(
        "batteries/<int:pk>/",
        views.BatteryDetailView.as_view(),
        name="battery-detail",
    ),

    path(
        "batteries/<int:pk>/edit/",
        views.BatteryUpdateView.as_view(),
        name="battery-update",
    ),

    path(
        "batteries/<int:pk>/delete/",
        views.BatteryDeleteView.as_view(),
        name="battery-delete",
    ),


# ===============================
# INVERTERS
# ===============================

    path(
        "inverters/",
        views.InverterListView.as_view(),
        name="inverter-list",
    ),

    path(
        "inverters/add/",
        views.InverterCreateView.as_view(),
        name="inverter-create",
    ),

    path(
        "inverters/<int:pk>/",
        views.InverterDetailView.as_view(),
        name="inverter-detail",
    ),

    path(
        "inverters/<int:pk>/edit/",
        views.InverterUpdateView.as_view(),
        name="inverter-update",
    ),

    path(
        "inverters/<int:pk>/delete/",
        views.InverterDeleteView.as_view(),
        name="inverter-delete",
    ),


# ===============================
# CHARGE CONTROLLERS
# ===============================

    path(
        "controllers/",
        views.ChargeControllerListView.as_view(),
        name="controller-list",
    ),

    path(
        "controllers/add/",
        views.ChargeControllerCreateView.as_view(),
        name="controller-create",
    ),

    path(
        "controllers/<int:pk>/",
        views.ChargeControllerDetailView.as_view(),
        name="controller-detail",
    ),

    path(
        "controllers/<int:pk>/edit/",
        views.ChargeControllerUpdateView.as_view(),
        name="controller-update",
    ),

    path(
        "controllers/<int:pk>/delete/",
        views.ChargeControllerDeleteView.as_view(),
        name="controller-delete",
    ),

# ===============================
# APPLIANCES
# ===============================

    path(
        "appliances/",
        views.ApplianceListView.as_view(),
        name="appliance-list",
    ),

    path(
        "appliances/add/",
        views.ApplianceCreateView.as_view(),
        name="appliance-create",
    ),

    path(
        "appliances/<int:pk>/",
        views.ApplianceDetailView.as_view(),
        name="appliance-detail",
    ),

    path(
        "appliances/<int:pk>/edit/",
        views.ApplianceUpdateView.as_view(),
        name="appliance-update",
    ),

    path(
        "appliances/<int:pk>/delete/",
        views.ApplianceDeleteView.as_view(),
        name="appliance-delete",
    ),
]