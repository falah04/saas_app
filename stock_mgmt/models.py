from django.db import models

# Create your models here.
class Supplier(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

class Part(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    reorder_threshold = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='parts')

class Order(models.Model):
    id = models.UUIDField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField()
    status = models.CharField(max_length=50)