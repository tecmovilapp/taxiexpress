from django.forms import ModelForm
from taxiadmin.models import Vehicle

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['register', 'number', 'year', 'vin', 'color', 'status', 'made', 'model']