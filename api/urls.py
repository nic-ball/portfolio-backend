from django.urls import path
from .views import ProjectList, ContactCreate

urlpatterns = [
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('contact/', ContactCreate.as_view(), name='contact-create'),
]
