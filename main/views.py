from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your view 

def index(request):
    #return HttpResponse('<h1>Carpool</h1>')
    return render(request, 'homepage.html')
def v1(respnse):
    return HttpResponse('<h1>View 1!</h1>')