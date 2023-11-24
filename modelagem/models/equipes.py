from django.db import models
from .participantes import Participantes
from .projetos import Projetos

class Equipes(models.Model):
    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"
        
    nome = models.CharField(max_length=50)
    membro = models.ManyToManyField(Participantes)
    projeto = models.ForeignKey(Projetos, related_name="equipes", on_delete=models.CASCADE)
    