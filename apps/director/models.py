from django.db import models

class Estudiante:
    pass
class Students(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    carrera = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    estrato = models.IntegerField(null=False)
    estado = models.BooleanField(blank=False, null=True)
    beneficio = models.BooleanField(blank=False, null=False)


    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):

    nombre = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)

    class Meta:
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"

    def __str__(self):
        return self.nombre


class Director(models.Model):

    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = "director"
        verbose_name_plural = "directores"

    def __str__(self):
        return self.nombre


class Asistente(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    rol = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = "asistentes"
        verbose_name_plural = "asistentes"

    def __str__(self):
        return self.nombre


class Convocatoria(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    fecha_apertura =models.DateField(null=False)
    fecha_clausura = models.DateField(null=False)

    class Meta:
        verbose_name = "convocatoria"
        verbose_name_plural = "convocatorias"

    def __str__(self):
        return self.nombre


class Duenos_cafeteria(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    tipo_cafeteria = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = "dueno_cafeteria"
        verbose_name_plural = "duenos_cafeteria"

    def __str__(self):
        return self.nombre

