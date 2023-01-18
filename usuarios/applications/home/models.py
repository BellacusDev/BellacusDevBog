from django.db import models

# apps terceros
from model_utils.models import TimeStampedModel



# Create your models here.


class Home(TimeStampedModel):
    """modelo de página principal"""
    title = models.CharField(
        'Nombre',
        max_length=30,
    )
    description = models.TextField()
    about_title = models.CharField(
        'Titulo Nosotros',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'Email de contacto',
        blank=True,
        null=True,
    )
    phone = models.CharField(
        'Teléfono contacto',
        max_length=20,
    )

    class Meta:
        verbose_name = 'Página Principal'
        verbose_name_plural = 'Página principal'

    def __str__(self):
        return self.title


class Suscribers(TimeStampedModel):
    """modelo de subscriptores"""
    email = models.EmailField()

    class Meta:
        verbose_name = 'Subscriptor'
        verbose_name_plural = 'Subscriptores'

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    """modelo de contactos"""
    full_name = models.CharField(
        'Nombres',
        max_length=60
    )
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.full_name
