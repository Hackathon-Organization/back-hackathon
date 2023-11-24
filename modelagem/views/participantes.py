from rest_framework.viewsets import ModelViewSet

from modelagem.models import Participantes
from modelagem.serializers import ParticipanteSerializers


class ParticipantesViewSet(ModelViewSet):
    queryset = Participantes.objects.all()
    serializer_class = ParticipanteSerializers