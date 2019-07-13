from django.db import models

# Create your models here.
class Habit(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=140, blank=True, default='')
    description = models.TextField()
    priority = models.IntegerField()

    
    