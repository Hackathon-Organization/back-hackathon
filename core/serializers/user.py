from rest_framework import serializers
from uploader.models import Image
from uploader.serializers import ImageSerializer
from django.contrib.auth.models import Group, Permission
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    logo_attachment_key = serializers.SlugRelatedField(
        source="logo",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    logo = ImageSerializer(required=False, read_only=True)
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True, required=False)
    user_permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True, required=False)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        logo_attachment_key = validated_data.pop('logo_attachment_key', None)
        groups_data = validated_data.pop('groups', [])
        user_permissions_data = validated_data.pop('user_permissions', [])

        # Remova 'logo' dos dados validados, pois será tratado separadamente
        logo_data = validated_data.pop('logo', None)

        # Crie o objeto User usando os campos necessários
        user = User.objects.create(**validated_data)

        # Se 'logo_attachment_key' for fornecido, crie o campo relacionado
        if logo_attachment_key:
            # Supondo que 'logo' é um campo relacionado, ajuste conforme necessário
            image = Image.objects.create(attachment_key=logo_attachment_key)
            user.logo = image
            user.save()

        # Use set para atribuir grupos e permissões de usuário
        user.groups.set(groups_data)
        user.user_permissions.set(user_permissions_data)

        return user
