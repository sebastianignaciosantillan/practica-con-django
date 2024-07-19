from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    edad = models.IntegerField()
    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=False)
    fecha_publicacion = models.DateField()
    GENERO_CHOICES = [
        ('Terror', 'Terror'),
        ('Accion', 'Accion'),
        ('Ciencia Ficcion', 'Ciencia Ficcion'),
        ('Romance', 'Romance'),
        ('Comedia', 'Comedia')
    ]
    genero = models.CharField(choices=GENERO_CHOICES, max_length=40)
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libro')
    def __str__(self) -> str:
        return f'Autor {self.autor.nombre} - {self.titulo}'
    
class Galeria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='img/')
    
    