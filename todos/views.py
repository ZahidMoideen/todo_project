from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project,Todo
from .forms import ProjectForm,TodoForm,TodoUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Customer



class ProjectListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'web/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        customer = Customer.objects.get(user=self.request.user)
        return Project.objects.filter(customer=customer)


class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = 'web/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['todos'] = project.todo_set.all()
        return context


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'web/create_project.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        # Get the Customer object associated with the logged-in user
        try:
            customer = Customer.objects.get(user=self.request.user)
            form.instance.customer = customer  # Set the customer field to the current user's customer
        except Customer.DoesNotExist:
            # If no customer is associated with the user, handle the case appropriately
            # You could raise an error, set a default value, or do something else
            raise Exception("Customer profile not found for the current user.")
        
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'web/update_project.html'
    success_url = reverse_lazy('project_list')


class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    template_name = 'web/delete_project.html'
    success_url = reverse_lazy('project_list')


class AddTodoView(LoginRequiredMixin,CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'web/add_todo.html'

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['project_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.kwargs['project_id']})


class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = Todo
    form_class = TodoUpdateForm
    template_name = 'web/update_todo.html'
    success_url = reverse_lazy('project_detail')

    def get_success_url(self):
        project_pk = self.object.project.pk
        return reverse_lazy('project_detail', kwargs={'pk': project_pk})


