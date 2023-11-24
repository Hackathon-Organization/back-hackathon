from rest_framework.viewsets import ModelViewSet

from modelagem.models import Patrocinador
from modelagem.serializers import PatrocinadorSerializers


class PatrocinadorViewSet(ModelViewSet):
    queryset = Patrocinador.objects.all()
    serializer_class = PatrocinadorSerializers