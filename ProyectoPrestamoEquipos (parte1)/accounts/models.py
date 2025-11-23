from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('asistente', 'Asistente'),
        ('estudiante', 'Estudiante'),
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES, default='estudiante')

    def __str__(self):
        return f"{self.usuario.username} ({self.rol})"
