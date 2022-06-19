from django.shortcuts import render
from . models import Car
from django.http import HttpResponse

# Create your views here.
def show_cars(request):
    cars = Car.objects.all().order_by('reg')
    return render(request, 'cars/show_cars.html', {'cars': cars})
def add_new_car(request):
    return render(request, 'cars/add_new_car.html')
def car_detail(request, slug):
    return HttpResponse()

