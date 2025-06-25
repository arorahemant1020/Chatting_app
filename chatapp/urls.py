from django.urls import path
from . import views

urlpatterns = [
    path('messages/<str:user1>/<str:user2>/', views.get_message_history),
]
