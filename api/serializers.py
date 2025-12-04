from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # Automagically grab all fields and convert them to JSON
        fields = '__all__'
        