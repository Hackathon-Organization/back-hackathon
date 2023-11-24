from django.db import models

class Avaliador(models.Model):
    class Meta:
        verbose_name = "Avaliador"
        verbose_name_plural = "Avaliadores"

    nome = models.CharField(max_length=50)
    area_de_especializacao = models.CharField(max_length=50)