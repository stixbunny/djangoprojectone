from django.http import Http404
from django.shortcuts import render
from .models import Property

def edificio(request):
    return render(request, 'properties.html')

def detail(request, property_id):
    try:
        property = Property.objects.get(pk=property_id)
    except Property.DoesNotExist:
        raise Http404("Esta propiedad no existe :(")
    context = {'property': property}
    return render(request, 'property.html', context)
