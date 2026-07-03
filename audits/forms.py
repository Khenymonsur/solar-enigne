from django import forms

from .models import Assessment


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






# from django import forms
#
# from .models import Appliance
#
#
# class ApplianceForm(forms.ModelForm):
#
#     class Meta:
#         model = Appliance
#
#         fields = [
#             "category",
#             "appliance_name",
#             "quantity",
#             "power_rating",
#             "surge_power",
#             "hours_per_day",
#             "critical_load",
#         ]
#
#     def __init__(self, *args, **kwargs):
#
#         super().__init__(*args, **kwargs)
#
#         for field in self.fields.values():
#
#             field.widget.attrs["class"] = "form-control"
#
#         self.fields["critical_load"].widget.attrs["class"] = "form-check-input"