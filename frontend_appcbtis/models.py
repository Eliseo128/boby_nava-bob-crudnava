from django.db import models

# Create your models here.
class Alumno(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    especialidad= models.CharField(max_length=100)
    promedio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.correo_electronico})"
    
    