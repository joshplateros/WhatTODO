from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    description = models.CharField(max_length=1000, help_text="Enter description of task")
    completed = models.BooleanField(default=False)
    due_date = models.DateField(default=timezone.now)
    due_date_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.description
