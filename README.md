# TaxiExpress

Sistema Web de geolocalización y reserva de taxis

## Getting Started

Sistema creado con Django 1.11.6

### Pre requisitos

Python 3.4   
Django 1.11.6

```
python -V
```

### Instalación

```
pip install virtualenv && pip install virtualenvwrapper
```

Crear nuevo ambiente virtual 'env3' haciendo referencia a python 3  
```
mkvirtualenv env3
```

Activar nuevo ambiente creado
```
workon env3
```

Desactivar ambiente
```
deactivate
```

Instalar django 1.11.6 en el ambiente virtual creado
```
pip install django==1.11.6
```

Crear nuevo proyecto vacio en django
```
django-admin startproject taxiexpress
```

Crear Archivo de Dependencias
```
pip freeze > requirements.txt
```

Instalar Todas las dependencias del archivo [requirements.txt](requirements.txt)
```
pip install -r requirements.txt
```