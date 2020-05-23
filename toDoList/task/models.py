from django.db import models
from datetime import datetime
# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    due_date = models.DateTimeField(default=datetime.now, null=False)