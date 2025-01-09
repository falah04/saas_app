from django.db import models

# Create your models here.
class MailConfig(models.Model):
    id = models.UUIDField(primary_key=True)
    smtp_server = models.CharField(max_length=255)
    port = models.IntegerField()
    use_tls = models.BooleanField()
    email = models.EmailField()

class Mail(models.Model):
    id = models.UUIDField(primary_key=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipient = models.EmailField()
    sender = models.EmailField()
    config = models.ForeignKey(MailConfig, on_delete=models.CASCADE, related_name='mails')