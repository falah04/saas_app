from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Task(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    assigned_to = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

class Document(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')