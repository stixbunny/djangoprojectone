from django.http import Http404
from django.shortcuts import render
from .models import Property, EntertainmentProperty, IndustrialProperty, ResidentialProperty

def edificio(request):
    EntProps = EntertainmentProperty.objects.all()
    IndProps = IndustrialProperty.objects.all()
    ResProps = ResidentialProperty.objects.all()
    context = {'EntProps': EntProps, 'IndProps': IndProps, 'ResProps': ResProps}
    return render(request, 'properties.html', context)

def detail_ent(request, property_id):
    try:
        property = EntertainmentProperty.objects.get(pk=property_id)
    except Property.DoesNotExist:
        raise Http404("Esta propiedad no existe :(")
    context = {'property': property}
    return render(request, 'property_ent.html', context)

def detail_ind(request, property_id):
    try:
        property = IndustrialProperty.objects.get(pk=property_id)
    except Property.DoesNotExist:
        raise Http404("Esta propiedad no existe :(")
    context = {'property': property}
    return render(request, 'property_ind.html', context)

def detail_res(request, property_id):
    try:
        property = ResidentialProperty.objects.get(pk=property_id)
    except Property.DoesNotExist:
        raise Http404("Esta propiedad no existe :(")
    context = {'property': property}
    return render(request, 'property_res.html', context)
