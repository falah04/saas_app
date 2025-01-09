from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    lead = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, related_name='leading_teams')

class Agent(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    email = models.EmailField()

class Intervention(models.Model):
    id = models.UUIDField(primary_key=True)
    description = models.TextField()
    date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='interventions')
    status = models.CharField(max_length=50)

class Fee(models.Model):
    id = models.UUIDField(primary_key=True)
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE, related_name='fees')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()