from django.urls import path
from . import views

name='prestamo'

urlpatterns = [
    path('', views.lista_prestamos, name='lista_prestamos'),
    path('crear/', views.crear_prestamo, name='crear_prestamo'),
    path('devolver/<int:prestamo_id>/', views.marcar_devolucion, name='devolver_prestamo'),
    path('reporte/pdf/', views.reporte_prestamos_pdf, name='reporte_prestamos_pdf'),
]
