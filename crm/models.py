from django.db import models

# Create your models here.
class CRMClient(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

class Contact(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    crm_client = models.ForeignKey(CRMClient, on_delete=models.CASCADE, related_name='contacts')

class Opportunity(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)
    crm_client = models.ForeignKey(CRMClient, on_delete=models.CASCADE, related_name='opportunities')