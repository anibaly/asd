from django.shortcuts import render, HttpResponse

def index(request):
    context = {"pelicula1": "Titanic",
               "pelicula2": "Up",
               "pelicula3": "El señor de los anillos"}
    return render(request, "index.html", context)

def contacto(request):
    return render(request, "contacto.html")

def ubicacion(request):
    return render(request, "ubicacion.html")

def calculadora(request):
    return render(request, "calculadora.html")

