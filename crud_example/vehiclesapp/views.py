from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from .models import Vehicle
from .forms import VehicleForm

def list_view(request):
    # Mostrar lista de vehículos
    dataset = Vehicle.objects.all()
    return render(request, "list_view.html", {'dataset': dataset})

def create_view(request):
    context = {}
    form = VehicleForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")  # Redirige a la lista después de guardar
    
    context['form'] = form
    return render(request, "create_view.html", context)

def update_view(request, id):
    context = {}
    object = get_object_or_404(Vehicle, id=id)
    form = VehicleForm(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context["form"] = form
    return render(request, "update_view.html", context)

# AGREGAR ESTA VISTA PARA ELIMINAR
def delete_view(request, id):
    context = {}
    object = get_object_or_404(Vehicle, id=id)
    
    if request.method == "POST":
        # Confirmar eliminación
        object.delete()
        return HttpResponseRedirect("/")
    
    context["object"] = object
    return render(request, "delete_view.html", context)