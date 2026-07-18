from django import forms

from .models import Quotation


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation

        fields = [
            "assessment",
            "customer",
            "installation_cost",
            "transport_cost",
            "discount",
            "vat",
            "status",
            "notes",
        ]

        widgets = {
            "assessment": forms.Select(attrs={"class": "form-select"}),
            "customer": forms.Select(attrs={"class": "form-select"}),

            "installation_cost": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "transport_cost": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "discount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "vat": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "status": forms.Select(attrs={"class": "form-select"}),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
        }