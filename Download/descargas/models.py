from django.db import models

class Descarga(models.Model):
    url = models.URLField()
    estado = models.CharField(max_length=20)
    progreso = models.IntegerField(default=0)
    fecha_inicio = models.DateField(auto_now_add=True)
