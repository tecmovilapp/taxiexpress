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
    #driver = forms.CharField(label=mark_safe('<a href="#" target="_blank">Conductor Asignado</a>'))
    driver = forms.CharField(label="Conductor Asignado", disabled=True)
    class Meta:
        model = Vehicle
        fields = ['id', 'register', 'number', 'year', 'vin', 'color', 'made', 'model', 'driver']
        readonly_fields = ('register',)

    def __init__(self, *args, **kwargs):
        super(VehicleForm,self).__init__(*args, **kwargs)
        self.fields['register'].widget.attrs['disabled'] = 'disabled'
        self.fields['number'].widget.attrs['disabled'] = 'disabled'
        self.fields['year'].widget.attrs['disabled'] = 'disabled'
        self.fields['vin'].widget.attrs['disabled'] = 'disabled'
        self.fields['color'].widget.attrs['disabled'] = 'disabled'
        self.fields['made'].widget.attrs['disabled'] = 'disabled'
        self.fields['model'].widget.attrs['disabled'] = 'disabled'
        try:
            driver = Driver.objects.get(vehicle=self.initial['id'])
            url = "/admin/taxiadmin/driver/%s/change"
            self.fields['driver'].initial = driver
            self.fields['driver'].help_text = mark_safe("<a href='{url}'>Ver</a>".format(url=url) % driver.id )
        except Driver.DoesNotExist:
            self.fields['driver'].initial = u'Sin Asignar'

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