from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "staff/",
        include("dashboard.urls"),
    ),

    path(
        "accounts/",
        include("accounts.urls"),
    ),

    path(
        "customers/",
        include("customers.urls"),
    ),

    path(
        "assessments/",
        include("audits.urls"),
    ),

    path(
        "equipment/",
        include("equipment.urls"),
    ),

    path(
        "reports/",
        include("reports.urls"),
    ),

    path(
        "portal/",
        include("customer_portal.urls"),
    ),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )