from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, AddTodoView,TodoUpdateView

urlpatterns = [
    path('projects/list/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='create_project'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='update_project'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('projects/<int:project_id>/add_todo/', AddTodoView.as_view(), name='add_todo'),
    path('projects/<int:pk>/update_todo/',TodoUpdateView.as_view(), name='update_todo'),
    
]
