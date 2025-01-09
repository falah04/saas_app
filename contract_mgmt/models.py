from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

class Contract(models.Model):
    id = models.UUIDField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contracts')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='invoices')
    issue_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

class Equipment(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    purchase_date = models.DateField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='equipments')