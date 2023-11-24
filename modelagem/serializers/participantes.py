from rest_framework.serializers import ModelSerializer, SlugRelatedField

from modelagem.models import Participantes

class ParticipanteSerializers(ModelSerializer):
    class Meta: 
        model = Participantes
        fields = "__all__"