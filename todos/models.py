from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from users.models import Customer


class Project(models.Model):
    project_id = models.CharField(max_length=120, unique=True)  
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    # ForeignKey to Customer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)

    def __str__(self):
        return self.title
    

class Todo(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    )
    todo_id = models.CharField(max_length=120, unique=True)  
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    
    def get_update_url(self):
        return reverse_lazy("update_todo", kwargs={"pk": self.pk})

