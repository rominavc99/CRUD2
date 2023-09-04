from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Curso(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
    
    class Meta:
        permissions = [
            ("can_view_curso", "Can view Curso"),
            ("can_edit_curso", "Can edit Curso"),
            ("can_delete_curso", "Can delete Curso"),
            ("can_add_curso", "Can add Curso"),
        ]
        
