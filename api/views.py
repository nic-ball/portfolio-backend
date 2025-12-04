from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

# ListAPIView allows Read-Only access
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_at') # Newest first
    serializer_class = ProjectSerializer
