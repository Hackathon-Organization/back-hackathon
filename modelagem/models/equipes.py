from django.db import models

# from .participantes import Participantes
# from .projetos import Projetos


class Equipes(models.Model):
    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    # nome da equipe
    nome = models.CharField(max_length=50)
    membro1 = models.CharField(max_length=100)
    membro2 = models.CharField(max_length=100)
    membro3 = models.CharField(max_length=100, blank=True, null=True)
    membro4 = models.CharField(max_length=100, blank=True, null=True)
    membro5 = models.CharField(max_length=100, blank=True, null=True)
    membro6 = models.CharField(max_length=100, blank=True, null=True)
    membro7 = models.CharField(max_length=100, blank=True, null=True)
    membro8 = models.CharField(max_length=100, blank=True, null=True)
    membro9 = models.CharField(max_length=100, blank=True, null=True)
    membro10 = models.CharField(max_length=100, blank=True, null=True)
    nota = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"({self.nome}) - {self.nota}"
