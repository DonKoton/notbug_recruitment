from django.urls import path

from todo import views

app_name = "todo"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('todos-list/', views.todos_list, name='todos_list'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]