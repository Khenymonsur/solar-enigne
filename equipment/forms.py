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



class BatteryForm(forms.ModelForm):

    class Meta:
        model = Battery
        fields = "__all__"

        widgets = {

            "manufacturer": forms.Select(
                attrs={"class": "form-select"}
            ),

            "model": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "battery_type": forms.Select(
                attrs={"class": "form-select"}
            ),

            "voltage": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "capacity_ah": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "cycle_life": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "active": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

        }



class InverterForm(forms.ModelForm):

    class Meta:
        model = Inverter
        fields = "__all__"

        widgets = {

            "manufacturer": forms.Select(
                attrs={"class": "form-select"}
            ),

            "model": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "capacity_kva": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.1",
                }
            ),

            "hybrid": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

            "voltage": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "efficiency": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "warranty": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "active": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

        }




class ChargeControllerForm(forms.ModelForm):

    class Meta:
        model = ChargeController
        fields = "__all__"

        widgets = {

            "manufacturer": forms.Select(
                attrs={"class": "form-select"}
            ),

            "model": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "controller_type": forms.Select(
                attrs={"class": "form-select"}
            ),

            "current_rating": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "voltage": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),

            "active": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

        }



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