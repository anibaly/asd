from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contacto',views.contacto,name="contacto"),
    path('ubicacion',views.ubicacion,name="ubicacion"),
    path("calculadora", views.calculadora,name="calculadora")
]
