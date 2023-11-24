from rest_framework.viewsets import ModelViewSet

from modelagem.models.avaliador import Avaliador
from modelagem.serializers.avaliador import AvaliadorSerializers


class AvaliadorViewSet(ModelViewSet):
    queryset = Avaliador.objects.all()
    serializer_class = AvaliadorSerializers