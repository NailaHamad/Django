# Generated by Django 5.0.3 on 2024-05-02 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmodule', '0003_task_rename_item_category_items_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(max_length=50),
        ),
    ]
