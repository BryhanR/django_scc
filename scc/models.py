from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class persona(models.Model): # TP

    nombre = models.CharField(max_length=30)
    apellido1 = models.CharField(max_length=30)
    apellido2 = models.CharField(max_length=30)
    id = models.OneToOneField(User,primary_key=True)#models.CharField(primary_key=True,max_length=9) # tratar de que sea estricto 9
    tipo = models.IntegerField(default=1) # 1 usuario 2 admin

    class Meta:
        db_table = 'persona'


class correspondencia(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha_recibido = models.DateField()
    oficio = models.CharField(max_length=40)
    fecha_oficio = models.DateField()
    destinatario = models.CharField(max_length=40)
    copia = models.TextField() # talvez si se crea una nueva tabla para tener varios destinatarios
    remitente = models.CharField(max_length=40)
    asunto = models.TextField()
    recibido = models.ForeignKey(persona)
    estado = models.CharField(max_length=100)
    observacion = models.TextField()
    adjunto = models.CharField(max_length=50)

    class Meta:
        db_table = 'correspondencia'



class enlace(models.Model):
    padre = models.ForeignKey('correspondencia',related_name='padre')
    hijo = models.ForeignKey('correspondencia',related_name='hijo')

    class Meta:
        db_table = 'enlace'



class alarma(models.Model):

    correspondencia = models.ForeignKey(correspondencia)
    fecha_maxima = models.DateTimeField()
    fecha_aviso = models.DateTimeField()
    realizado = models.BooleanField(default=False)

    class Meta:
        db_table = 'alarma'


