from rest_framework.serializers import ModelSerializer, SlugRelatedField

from modelagem.models.tecnologia import Tecnologias

class TecnologiaSerializers(ModelSerializer):
    class Meta: 
        model = Tecnologias
        fields = "__all__"