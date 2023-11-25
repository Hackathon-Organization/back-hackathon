from django.db import models

from .equipes import Equipes
from .avaliador import Avaliador

class Avaliacao(models.Model):   
    nota = models.DecimalField(max_digits=1000, decimal_places=2)
    equipe = models.ForeignKey(Equipes, on_delete=models.CASCADE)
    avaliador = models.ForeignKey(Equipes, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nota