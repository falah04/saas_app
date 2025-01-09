from django.db import models

# Create your models here.
class ChatSession(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    id = models.UUIDField(primary_key=True)
    content = models.TextField()
    sent_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='messages')
    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    timestamp = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    id = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()