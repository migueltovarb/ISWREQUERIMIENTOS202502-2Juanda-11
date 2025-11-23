from django.urls import path
from .views import registrar_usuario, iniciar_sesion, cerrar_sesion

app_name = 'accounts'

urlpatterns = [
    path('registro/', registrar_usuario, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]
