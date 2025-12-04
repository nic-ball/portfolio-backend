from rest_framework import serializers
from .models import Project, ContactMessage

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # Automagically grab all fields and convert them to JSON
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
