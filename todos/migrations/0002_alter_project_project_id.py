# Generated by Django 5.0.4 on 2024-04-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
