from django import forms

from equipment.models import Appliance


class ApplianceForm(forms.ModelForm):

    class Meta:
        model = Appliance

        fields = "__all__"

        widgets = {
            "category": forms.Select(
                attrs={"class": "form-select"}
            ),

            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "default_wattage": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "surge_factor": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "default_hours": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "energy_efficient": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

            "active": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }