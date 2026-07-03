from django.contrib import admin

from .models import Assessment, Appliance


class ApplianceInline(admin.TabularInline):
    model = Appliance
    extra = 1
    show_change_link = True


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):

    list_display = (
        "project_name",
        "customer",
        "status",
        "completion_percentage",
        "backup_hours",
        "system_voltage",
        "created_at",
    )

    list_filter = (
        "status",
        "system_voltage",
        "created_at",
    )

    search_fields = (
        "project_name",
        "customer__full_name",
        "customer__company_name",
        "customer__phone",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        ApplianceInline,
    ]

    fieldsets = (

        (
            "Project Information",
            {
                "fields": (
                    "customer",
                    "project_name",
                    "status",
                    "completion_percentage",
                )
            },
        ),

        (
            "Design Parameters",
            {
                "fields": (
                    "backup_hours",
                    "system_voltage",
                    "peak_sun_hours",
                )
            },
        ),

        (
            "Engineering Result",
            {
                "fields": (
                    "connected_load",
                    "daily_energy",
                )
            },
        ),

        (
            "Report",
            {
                "fields": (
                    "report_generated",
                )
            },
        ),

        (
            "Audit Trail",
            {
                "classes": (
                    "collapse",
                ),
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),

    )







# from django.contrib import admin
# from .models import Assessment, Appliance
#
#
# class ApplianceInline(admin.TabularInline):
#     model = Appliance
#     extra = 1
#
#
# @admin.register(Assessment)
# class AssessmentAdmin(admin.ModelAdmin):
#
#     list_display = (
#         "project_name",
#         "customer",
#         "backup_hours",
#         "system_voltage",
#         "created_at",
#     )
#
#     inlines = [
#         ApplianceInline,
#     ]