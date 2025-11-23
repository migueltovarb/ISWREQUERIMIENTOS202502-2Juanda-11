from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.lista_equipos, name='lista'),
    path('registrar/', views.registrar_equipo, name='registrar_equipo'),
    path('reporte/pdf/', views.reporte_equipos_pdf, name='reporte_equipos_pdf'),
]
