from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskView, name="task-list"),
    path('task-detail/<str:pk>/', views.detailTaskView, name="task-detail"),
    path('task-update/<str:pk>/', views.updateTask, name="task-update"),
    path('task-delete/<str:pk>/', views.deleteTask, name="task-delete"),
    path('task-create/', views.createTask, name="create-task")
]
