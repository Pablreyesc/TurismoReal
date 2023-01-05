from dataclasses import fields
from django import forms
from .models import Departamento, Reserva

class DeptoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'




