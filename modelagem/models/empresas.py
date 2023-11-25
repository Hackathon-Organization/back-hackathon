from django.db import models

from .avaliador import Avaliador

class Empresa(models.Model):
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    nome = models.CharField(max_length=50)
    contato = models.EmailField()
    funcao = models.CharField(max_length=50)
    avaliador = models.ForeignKey(Avaliador, related_name="Empresa", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome