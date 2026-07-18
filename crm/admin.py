from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    list_display = (
        "reference",
        "full_name",
        "state",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "state",
    )

    search_fields = (
        "reference",
        "full_name",
        "email",
        "phone",
    )