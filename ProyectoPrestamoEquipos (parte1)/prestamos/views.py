from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Prestamo
from inventario.models import Equipo
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.utils import timezone

@login_required
def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos/lista.html', {'prestamos': prestamos})

@login_required
def crear_prestamo(request):
    equipos = Equipo.objects.all()

    if request.method == 'POST':
        equipo_id = request.POST.get('equipo')
        equipo = get_object_or_404(Equipo, id=equipo_id)

        Prestamo.objects.create(
            equipo=equipo,
            usuario=request.user
        )

        return redirect('prestamos:lista_prestamos')

    return render(request, 'prestamos/crear.html', {'equipos': equipos})

@login_required
def marcar_devolucion(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    prestamo.devuelto = True
    prestamo.save()
    return redirect('lista_prestamos')

def reporte_prestamos_pdf(request):
    # Crear archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_prestamos.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    y = height - 50
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Reporte de Préstamos")

    y -= 40
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Equipo")
    p.drawString(200, y, "Usuario")
    p.drawString(350, y, "Fecha")
    p.drawString(450, y, "Devuelto")

    y -= 20
    p.line(50, y, 550, y)
    y -= 30

    p.setFont("Helvetica", 11)
    prestamos = Prestamo.objects.all()

    for pmo in prestamos:
        if y < 80:  # Crear nueva página si ya no cabe más
            p.showPage()
            y = height - 50

        p.drawString(50, y, pmo.equipo.nombre)
        p.drawString(200, y, pmo.usuario.username)
        p.drawString(350, y, pmo.fecha_prestamo.strftime("%Y-%m-%d"))
        p.drawString(450, y, "Sí" if pmo.devuelto else "No")

        y -= 25

    p.save()
    return response