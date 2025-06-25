import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproj.settings')  # Replace 'chatapp' with your actual project name
django.setup()

from django.contrib.auth.models import User

def create_users():
    users = [
        {"username": "naman", "password": "1234"},
        {"username": "shubh", "password": "1234"},
        {"username": "priya", "password": "1234"},
    ]

    for user_data in users:
        user, created = User.objects.get_or_create(username=user_data["username"])
        if created:
            user.set_password(user_data["password"])
            user.save()
            print(f"Created user: {user.username}")
        else:
            print(f"User already exists: {user.username}")

if __name__ == '__main__':
    create_users()
