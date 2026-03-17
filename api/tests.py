from rest_framework.test import APITestCase
from rest_framework import status
from .models import ContactMessage

class ContactApiTests(APITestCase):
    def test_create_contact_message(self):
        """Ensure we can create a new contact message."""
        url = '/api/contact/'
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        }
        # mock a POST request from the React frontend
        response = self.client.post(url, data, format='json')

        # Check API returns 201 created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check message is saved to the database
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.get().name, 'Test User')

    def test_create_contact_message_invalid_email(self):
        """Ensure the API rejects bad emails"""
        url = '/api/contact/'
        data = {
            'name': 'Test User',
            'email': 'not-an-email',
            'message': 'Hello'
        }
        response = self.client.post(url, data, format='json')

        # Should return 400 Bad request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Database should remain empty
        self.assertEqual(ContactMessage.objects.count(), 0)
        