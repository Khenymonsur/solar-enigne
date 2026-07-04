from django import forms

from .models import (
    Assessment,
    Appliance,
)


class AssessmentForm(forms.ModelForm):

    class Meta:

        model = Assessment

        fields = [

            "customer",
            "project_name",
            "backup_hours",
            "system_voltage",
            "peak_sun_hours",
            "status",

        ]

        widgets = {

            "customer": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "project_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Country Home Installation",
                }
            ),

            "backup_hours": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                }
            ),

            "system_voltage": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "peak_sun_hours": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.1",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

        }

    def clean_backup_hours(self):

        value = self.cleaned_data["backup_hours"]

        if value <= 0:

            raise forms.ValidationError(
                "Backup hours must be greater than zero."
            )

        return value

    def clean_peak_sun_hours(self):

        value = self.cleaned_data["peak_sun_hours"]

        if value <= 0:

            raise forms.ValidationError(
                "Peak sun hours must be greater than zero."
            )

        return value



class ApplianceForm(forms.ModelForm):

    class Meta:

        model = Appliance

        fields = (
            "library_appliance",
            "quantity",
            "critical_load",
            "simultaneous",
        )

        widgets = {

            "library_appliance": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                }
            ),

            "critical_load": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "simultaneous": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

        }