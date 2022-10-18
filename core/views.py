from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
        return render(request, "core/home.html")

def porque_adoptar(request):
        return render(request, "core/porque_adoptar.html")
    
def formulario_de_adopcion(request):
        return render(request, "core/formulario_de_adopcion.html")

def como_adoptar(request):
        return render(request, "core/como_adoptar.html")