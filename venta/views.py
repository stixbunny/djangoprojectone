from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contact.html')

def acerca(request):
    return render(request, 'about.html')
