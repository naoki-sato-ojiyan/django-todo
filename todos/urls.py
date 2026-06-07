from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'), 
    path('complete/<int:pk>/', views.todo_complete, name='todo_complete'),  # ← 新規追加

]