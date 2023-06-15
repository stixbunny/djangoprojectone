from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def edificio(request):
    return render(request, 'properties.html')

def contacto(request):
    return render(request, 'contact.html')

def acerca(request):
    return render(request, 'about.html')
