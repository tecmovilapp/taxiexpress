from django import forms
from django.forms import ModelForm, Form
from taxiadmin.models import Vehicle, Driver
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField, HiddenInput

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        html =  Template("""<img src="$link" width="200" height="200"/>""")
        return mark_safe(html.substitute(link=value))

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['register', 'number', 'year', 'vin', 'color', 'made', 'model']

class DriverForm(forms.ModelForm):
    #picture = ImageField(widget=PictureWidget) # TODO: To add an image to picture field, try to modify so it can be edited too, with this it only displays the image on the form  
    class Meta:
        model = Driver        
        #exclude = ['vehicle',]
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(DriverForm, self).__init__(*args, **kwargs)
        #self.fields['vehicle'].queryset = Vehicle.objects.filter(year=2016)
        if not (kwargs.get('instance') is None):
            self.fields['vehicle'].queryset = Vehicle.objects.exclude(id__in = Driver.objects.exclude(vehicle = self.initial['vehicle']).values_list('vehicle', flat=True)) 
        else:
            self.fields['vehicle'].queryset = Vehicle.objects.exclude(id__in = Driver.objects.all().values_list('vehicle', flat=True))
            #self.fields['picture'].widget = HiddenInput() #Hide Input Defined on Model

class MyForm(forms.Form):
    num1 = forms.CharField(max_length=20, help_text='Seleccione el conductor a quien se asignara esta carrera', label="Conductor")
    num2 = forms.CharField(max_length=20)
    result = forms.CharField(max_length=20)