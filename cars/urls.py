from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_cars, name= 'show_cars'),
    path(r'^(?P<slug>[\w-]+)/$', views.car_detail, name='car_detail'),
    path('add_new_car/', views.add_new_car, name='add_new_car'),
]

