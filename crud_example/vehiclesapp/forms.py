from django import forms
from .models import Vehicle

# creating a form
class VehicleForm(forms.ModelForm):

    #create meta class
    class Meta:
        # specify model to be used
        model = Vehicle

        # specify fields to be used
        fields = [
            "placa",
            "marca",
            "modelo",
            "color",  # CAMBIADO: de "color_vehicle" a "color"
        ]

        labels = {
            "placa": "Número de placa",
            "marca": "Marca del vehículo", 
            "modelo": "Modelo del vehículo",
            "color": "Color del Vehículo",  # CAMBIADO: de "color_vehicle" a "color"
        }

        widgets = {
            "placa": forms.TextInput(attrs={"class": "form-control"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.NumberInput(attrs={"class": "form-control"}),  # Cambiado a NumberInput
            "color": forms.Select(attrs={"class": "form-control"}),  # CAMBIADO: Select para choices
        }