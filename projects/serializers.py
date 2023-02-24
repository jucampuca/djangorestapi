# Usamos nuestro archivo para llamar un modelo despecial de rest framework
from rest_framework import serializers

# Aca vamos a indicarle que sto esta basado en un modelo previamente creado
from .models import Project

# Aca creamos nuestro serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )