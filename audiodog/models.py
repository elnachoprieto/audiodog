from django.db import models

# Create your models here.

from django.utils import timezone

class Cancion(models.Model):

    cancion = models.CharField(max_length=200)
    artista = models.TextField(max_length=100)
    duracion = models.CharField(max_length=5)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE, null=False)

    registro_fecha = models.DateTimeField(
            default=timezone.now)

    def crear(self):
        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.cancion

class Usuario(models.Model):

    REGION = [
        (1, 'Arica y Parinacota'),
        (2, 'Tarapacá'),
        (3, 'Antofagasta'),
        (4, 'Atacama'),
        (5, 'Coquimbo'),
        (6, 'Valparaíso'),
        (7, 'Metropolitana'),
        (8, 'O''Higgins'),
        (9, 'Maule'),
        (10, 'Ñuble'),
        (11, 'Biobio'),
        (12, 'Araucanía'),
        (13, 'Los Rïos'),
        (14, 'Los Lagos'),
        (15, 'Aisén'),
        (16, 'Magallanes'),
    ]

    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rut = models.CharField(max_length=10)
    email = models.TextField(max_length=100)
    nacimiento_fecha = models.DateTimeField(
            default=timezone.now)
    telefonos = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    registro_fecha = models.DateTimeField(
            default=timezone.now)

    def crear(self):
        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.usuario

class Region(models.Model):

    region = models.CharField(max_length=100)
    registro_fecha = models.DateTimeField(
            default=timezone.now)

    def crear(self):
        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return str(self.region)

class Ciudad(models.Model):

    ciudad = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    registro_fecha = models.DateTimeField(
            default=timezone.now)

    def crear(self):
        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return str(self.ciudad)

class Pais(models.Model):

    pais = models.CharField(max_length=100)
    gentilicio = models.TextField(max_length=100)
    registro_fecha = models.DateTimeField(
            default=timezone.now)

    def crear(self):
        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.pais
