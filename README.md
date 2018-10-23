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
mkvirtualenv env3 #Si unicamente se tiene instalado python 3 
mkvirtualenv -p python3 env3 #para crear el ambiente especificamente con python 3 en caso de que hayan mas instalaciones de python
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

Instalar django-suit v2
```
pip install https://github.com/darklow/django-suit/tarball/v2
```

Archivo de configuracion para Visual Code
[vs.settings.json](vs.settings.json)

Se deben colectar todos los archivos estaticos para que trabaje el django suit
```
python manage.py collectstatic
```