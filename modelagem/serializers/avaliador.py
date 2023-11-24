from rest_framework.serializers import ModelSerializer, SlugRelatedField

from modelagem.models.avaliador import Avaliador

class AvaliadorSerializers(ModelSerializer):
    class Meta: 
        model = Avaliador
        fields = "__all__"