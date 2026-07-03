from django import forms

from .models import (
    Manufacturer,
    SolarPanel,
    Battery,
    Inverter,
    ChargeController,
)


class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "website": forms.URLInput(attrs={"class": "form-control"}),
            "support_email": forms.EmailInput(attrs={"class": "form-control"}),
            "support_phone": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class SolarPanelForm(forms.ModelForm):

    class Meta:
        model = SolarPanel
        fields = "__all__"

        widgets = {

            "manufacturer": forms.Select(
                attrs={"class": "form-select"}
            ),

            "model": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "wattage": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "efficiency": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "warranty": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "active": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

        }