from django.db import models

class activity(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    class Meta:
        app_label = 'taskmodule'

class items(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    class Meta:
        app_label = 'taskmodule'

class task(models.Model):
    name = models.CharField(max_length=50)
    priority = models.CharField(max_length=10)
    category = models.CharField(max_length=50)

    class Meta:
        app_label = 'taskmodule'

