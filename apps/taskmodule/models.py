from django.db import models

class activity(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    class Meta:
        app_label = 'taskmodule'
