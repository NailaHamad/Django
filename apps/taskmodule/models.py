from django.db import models

class Task(models.Model):
    Task_Name = models.CharField()
    Task_Priority = models.CharField()
    Task_Section = models.CharField()
    
