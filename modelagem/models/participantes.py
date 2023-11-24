from django.db import models

class Participantes(models.Model):
    class Meta:
        verbose_name = "Particiante"
        verbose_name_plural = "Participantes"
        
    nome = models.CharField(max_length=50)
