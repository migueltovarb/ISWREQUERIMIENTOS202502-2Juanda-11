from django.shortcuts import render, redirect
from .forms import EquipoForm
from .models import Equipo
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'inventario/lista_equipos.html', {'equipos': equipos})

def registrar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventario:lista')
    else:
        form = EquipoForm()

    return render(request, 'inventario/registrar_equipo.html', {'form': form})

def reporte_equipos_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_equipos.pdf"'

    p = canvas.Canvas(response, pagesize=letter)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, "Reporte de Equipos")

    p.setFont("Helvetica", 12)

    y = 720
    equipos = Equipo.objects.all()

    for equipo in equipos:
        linea = f"{equipo.nombre} | Total: {equipo.cantidad_total} | Disponible: {equipo.cantidad_disponible}"
        p.drawString(40, y, linea)
        y -= 20
        if y < 50:  
            p.showPage()
            y = 750
            p.setFont("Helvetica", 12)

    p.showPage()
    p.save()

    return response
