# Generated by Django 5.0.4 on 2024-04-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.BooleanField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')]),
        ),
    ]
