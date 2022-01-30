from django import forms
from cars.models import Car, Parts


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            'brand': forms.TextInput(attrs={"placeholder": "Volkswagen/Renault etc."}),
            'model': forms.TextInput(attrs={"placeholder": "Golf/Megane etc."}),
            'prod_year': forms.TextInput(attrs={"placeholder": "YYYY"}),
            'owner': forms.TextInput(attrs={"placeholder": "your name"}),
        }


class PartsList(forms.ModelForm):
    class Meta:
        model = Parts
        exclude = ('car',)
        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "name of part"}),
            'producer': forms.TextInput(attrs={"placeholder": "producer of part"}),
            'part_number': forms.TextInput(attrs={"placeholder": "part number"}),
            'price': forms.TextInput(attrs={"placeholder": "price"}),
            'date_of_service': forms.TextInput(attrs={"placeholder": "date of service"}),
            'mileage': forms.TextInput(attrs={"placeholder": "actual mileage"}),
        }
