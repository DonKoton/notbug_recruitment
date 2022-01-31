from django import forms
from cars.models import Car, Parts


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            'brand': forms.TextInput(attrs={
                "placeholder": "Volkswagen/Renault etc.",
                "class": "form-control"
            }),
            'model': forms.TextInput(attrs={
                "placeholder": "Golf/Megane etc.",
                "class": "form-control"
            }),
            'prod_year': forms.TextInput(attrs={
                "placeholder": "YYYY",
                "class": "form-control"
            }),
            'owner': forms.TextInput(attrs={
                "placeholder": "your name",
                "class": "form-control"
            }),
        }


class PartsList(forms.ModelForm):
    class Meta:
        model = Parts
        exclude = ('car',)
        widgets = {
            'name': forms.TextInput(attrs={
                "placeholder": "name of part",
                "class": "form-control"
            }),
            'producer': forms.TextInput(attrs={
                "placeholder": "producer of part",
                "class": "form-control"
            }),
            'part_number': forms.TextInput(attrs={
                "placeholder": "part number",
                "class": "form-control"
            }),
            'price': forms.TextInput(attrs={
                "placeholder": "price",
                "class": "form-control"
            }),
            'date_of_service': forms.TextInput(attrs={
                "placeholder": "date of service",
                "class": "form-control"
            }),
            'mileage': forms.TextInput(attrs={
                "placeholder": "actual mileage",
                "class": "form-control"
            }),
        }
