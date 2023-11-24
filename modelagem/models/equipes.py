from django.db import models
from .participantes import Participantes
from .projetos import Projetos

class Equipes(models.Model):
    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"
        
    #nome da equipe
    nome = models.CharField(max_length=50)
    #membros da equipe
    membro = models.ForeignKey(Participantes, related_name="equipes", on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projetos, related_name="equipes", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome} - {self.projeto}"