import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproj.settings') 
django.setup()

from django.contrib.auth.models import User
from chatapp.models import Message  

def seed():
    hemant, _ = User.objects.get_or_create(username='hemant')
    arjun, _ = User.objects.get_or_create(username='arjun')

    Message.objects.create(sender=hemant, receiver=arjun, content="Hey Arjun!")
    Message.objects.create(sender=arjun, receiver=hemant, content="Hey Hemant! What's up?")
    Message.objects.create(sender=hemant, receiver=arjun, content="All good. Just testing our chat API.")
    Message.objects.create(sender=arjun, receiver=hemant, content="Well that's great. Is it working?")
    Message.objects.create(sender=hemant, receiver=arjun, content="It sure is working perfectly")

    print("Messages seeded successfully.")

def seed():

    u1, _ = User.objects.get_or_create(username='naman')
    u2, _ = User.objects.get_or_create(username='priya')

    Message.objects.create(sender=u1, receiver=u2, content="Hey Priya!")
    Message.objects.create(sender=u2, receiver=u1, content="Hey Naman! How are ypu doing?")
    Message.objects.create(sender=u1, receiver=u2, content="I'm doing well Priya. What about you?")
    Message.objects.create(sender=u2, receiver=u1, content="I'm doing well too. Thanks for asking.")
    Message.objects.create(sender=u1, receiver=u2, content="Glad to hear that!")

    print("Messages seeded successfully.")
    
if __name__ == '__main__':
    seed()
