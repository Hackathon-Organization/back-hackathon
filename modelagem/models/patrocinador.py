from django.db import models

from uploader.models import Image

class Patrocinador(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ForeignKey (
        Image,
        related_name="+",
        on_delete=models.PROTECT,
    )
    investimento = models.DecimalField(max_digits=1000, decimal_places=5)