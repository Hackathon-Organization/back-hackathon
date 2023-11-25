from django.db import models

from .equipes import Equipes
from core.models import User

class Membros(models.Model):
    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"
        
    quantidade = models.BooleanField()
    equipe = models.ForeignKey(Equipes, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nome} - {self.projeto}"