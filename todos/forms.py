from django import forms
from .models import Project, Todo

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_id', 'title', 'description']
        labels = {
            'project_id': 'Project ID',
            'title': 'Title',
            'description': 'Description',
        }


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_id','title', 'description',]
        labels = {
            'todo_id':'Todo ID',
            'title': 'Title',
            'description': 'Description',
           
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_id','title', 'description', 'status']
        labels = {
            'todo_id':'Todo ID',
            'title': 'Title',
            'description': 'Description',
            'status': 'Status',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
