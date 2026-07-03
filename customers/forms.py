from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = [
            "full_name",
            "company_name",
            "email",
            "phone",
            "whatsapp",
            "address",
            "state",
            "city",
            "building_type",
        ]

        widgets = {
            "address": forms.Textarea(
                attrs={
                    "rows": 3,
                }
            )
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update(
                {
                    "class": "form-control",
                }
            )