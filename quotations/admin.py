from django.contrib import admin

from .models import Quotation, QuotationItem


class QuotationItemInline(admin.TabularInline):
    model = QuotationItem
    extra = 0


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):

    list_display = (
        "quotation_no",
        "customer",
        "assessment",
        "status",
        "grand_total",
        "issue_date",
    )

    list_filter = (
        "status",
        "issue_date",
    )

    search_fields = (
        "quotation_no",
        "customer__full_name",
    )

    readonly_fields = (
        "quotation_no",
        "issue_date",
        "grand_total",
    )

    inlines = [
        QuotationItemInline,
    ]


@admin.register(QuotationItem)
class QuotationItemAdmin(admin.ModelAdmin):

    list_display = (
        "quotation",
        "description",
        "quantity",
        "unit_price",
        "total",
    )