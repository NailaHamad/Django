# Generated by Django 5.0.3 on 2024-05-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmodule', '0004_alter_activity_category_alter_activity_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.FloatField(default=0.0),
        ),
    ]