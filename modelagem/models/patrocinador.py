from django.db import models

from uploader.models import Image

class Patrocinador(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    investimento = models.DecimalField(max_digits=1000, decimal_places=5)
    
    def __str__(self):
        return self.nome