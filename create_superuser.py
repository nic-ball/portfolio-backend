import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

User = get_user_model()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME','admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'thisIsNotTheWay69!')

if not User.objects.filter(username=username).exists():
    print(F"Creating superuser: {username}")
    User.objects.create_superuser(username, email, password)
    print("Superuser created successfully.")
else:
    print(f"Superuser {username} already exists.")
