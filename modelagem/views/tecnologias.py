from rest_framework.viewsets import ModelViewSet

from modelagem.models.tecnologia import Tecnologias
from modelagem.serializers.tecnologias import TecnologiaSerializers


class TecnologiasViewSet(ModelViewSet):
    queryset = Tecnologias.objects.all()
    serializer_class = TecnologiaSerializers