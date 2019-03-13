from django import forms
from django.forms import ModelForm, Form
from taxiadmin.models import Vehicle

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['register', 'number', 'year', 'vin', 'color', 'made', 'model']

class MyForm(forms.Form):
    num1 = forms.CharField(max_length=20, help_text='Seleccione el conductor a quien se asignara esta carrera', label="Conductor")
    num2 = forms.CharField(max_length=20)
    result = forms.CharField(max_length=20)