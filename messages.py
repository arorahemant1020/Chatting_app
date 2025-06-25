import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproj.settings') 
django.setup()

from django.contrib.auth.models import User
from chatapp.models import Message  

def seed():
    u5, _ = User.objects.get_or_create(username='hemant')
    u6, _ = User.objects.get_or_create(username='arjun')

    Message.objects.create(sender=u5, receiver=u6, content="Hey Arjun!")
    Message.objects.create(sender=u6, receiver=u5, content="Hey Hemant! What's up?")
    Message.objects.create(sender=u5, receiver=u6, content="All good. Just testing our chat API.")
    Message.objects.create(sender=u6, receiver=u5, content="Well that's great. Is it working?")
    Message.objects.create(sender=u5, receiver=u6, content="It sure is working perfectly")

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

def seed():

    u3, _ = User.objects.get_or_create(username='hemant')
    u4, _ = User.objects.get_or_create(username='shubh')

    Message.objects.create(sender=u3, receiver=u4, content="Hello Shubh! Welcome to our company.")
    Message.objects.create(sender=u4, receiver=u3, content="Hey Hemant! Thank you for giving me the opportunity.")

    print("Messages seeded successfully.")
    
if __name__ == '__main__':
    seed()
