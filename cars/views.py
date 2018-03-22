from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import pyrebase
# Create your views here.


config = {
  "apiKey": "AIzaSyAI755venVr58C5F1wExAlItIbyYFv98TQ",
  "authDomain": "taxiexpress-ceb3f.firebaseapp.com",
  "databaseURL": "https://taxiexpress-ceb3f.firebaseio.com",
  "projectId" : "taxiexpress-ceb3f",
  "storageBucket": "taxiexpress-ceb3f.appspot.com"
}



def index(request):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    # To save data with a unique, auto-generated, timestamp-based key, use the push() method.
    # data = {"name": "Mortimer 'Morty' Smith"}
    # db.child("users").push(data)

    # To create your own keys use the set() method. The key in the example below is "Morty".
    data = {"placa": "PBC 4554", "anio": "2010", "marca": "Toyota", "modelo": "Corolla"}
    db.child("cars").child("1").set(data)

    context = {'': ''}
    return render(request, 'cars/index.html', context)

def detail(request, car_id):
    #car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/detail.html', {'car': '1'})
