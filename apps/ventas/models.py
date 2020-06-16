from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    precio = models.CharField(max_length = 220, blank = False, null = False)
    cantidad = models.CharField(max_length = 100, blank = False, null = False)
    montoadicional = models.TextField(blank = False,null = False)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
