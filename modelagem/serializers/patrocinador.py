from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from modelagem.models import Patrocinador

class PatrocinadorSerializers(ModelSerializer):
    class Meta:
        model = Patrocinador
        fields = "__all__"
        ordering = ['logo']

    logo_attachment_key = SlugRelatedField(
        source="logo",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    logo = ImageSerializer(required=False, read_only=True)
