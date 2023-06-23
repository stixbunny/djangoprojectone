from django.http import Http404
from django.shortcuts import render
from .models import Property, EntertainmentProperty, IndustrialProperty, ResidentialProperty
from django.shortcuts import redirect

def edificio(request):
    EntProps = EntertainmentProperty.objects.filter(is_visible = True)
    IndProps = IndustrialProperty.objects.filter(is_visible = True)
    ResProps = ResidentialProperty.objects.filter(is_visible = True)
    context = {'EntProps': EntProps, 'IndProps': IndProps, 'ResProps': ResProps}
    return render(request, 'properties.html', context)

def detail_ent(request, property_id):
    if request.method == "POST":
        buy_property(request.POST['property_id'], 'ent')
    try:
        property = EntertainmentProperty.objects.get(pk = property_id)
    except Property.DoesNotExist:
        raise Http404("Esta propiedad no existe :(")
    context = {'property': property}
    return render(request, 'property_ent.html', context)

def detail_ind(request, property_id):
    if request.method == "POST":
        buy_property(request.POST['property_id'], 'ind')
    try:
        property = IndustrialProperty.objects.get(pk = property_id)
    except Property.DoesNotExist:
        raise Http404("Esta propiedad no existe :(")
    context = {'property': property}
    return render(request, 'property_ind.html', context)

def detail_res(request, property_id):
    if request.method == "POST":
        buy_property(request.POST['property_id'], 'res')
    try:
        property = ResidentialProperty.objects.get(pk = property_id)
    except Property.DoesNotExist:
        raise Http404("Esta propiedad no existe :(")
    context = {'property': property}
    return render(request, 'property_res.html', context)

def buy_property(property_id, type):
    if type == 'ind':
        property = IndustrialProperty.objects.get(pk=property_id)
        property.is_visible = False
        property.save()
        return redirect(edificio)
    elif type == 'ent':
        property = EntertainmentProperty.objects.get(pk=property_id)
        property.is_visible = False
        property.save()
        return redirect(edificio)
    elif type == 'res':
        property = ResidentialProperty.objects.get(pk=property_id)
        property.is_visible = False
        property.save()
        return redirect(edificio)