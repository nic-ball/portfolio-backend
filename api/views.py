from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, ContactMessage
from .serializers import ProjectSerializer, ContactSerializer

# ListAPIView allows Read-Only access
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_at') # Newest first
    serializer_class = ProjectSerializer

class ContactCreate(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        # Save to db
        serializer.save()
        # Send email notification to site admin
        # Console in dev, will send REAL email in Production
        data = serializer.validated_data
        print(f"------------\nNEW MESSAGE RECIEVED:\nFrom: {data['name']} ({data['email']})\nMessage: {data['message']}\n------------")

        # Uncomment send_mail below to enable real email sending in production
        ...

        # send_mail(
        #     subject=f"Portfolio Contact: {data['name']}",
        #     message=f"From: {data['email']}\n\n{data['message']}",
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[settings.ADMIN_EMAIL],
        #     fail_silently=False,
        # )

        ...
