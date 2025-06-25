from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Message

def get_message_history(request, user1, user2):
    try:
        sender = User.objects.get(username=user1)
        receiver = User.objects.get(username=user2)
    except User.DoesNotExist:
        return JsonResponse({'error': 'One or both users not found'}, status=404)

    messages = Message.objects.filter(
        sender__in=[sender, receiver],
        receiver__in=[sender, receiver]
    ).order_by('timestamp')


    formatted = ""
    for msg in messages:
        formatted += f"{msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {msg.sender.username} -> {msg.receiver.username}:\n{msg.content}\n\n"

    return HttpResponse(formatted, content_type="text/plain")
