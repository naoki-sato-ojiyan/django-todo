from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # ← 新規追加
from .models import Todo

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Todo.objects.create(user=request.user, title=title)
        return redirect('todo_list')
    return render(request, 'todos/todo_create.html')

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})

@login_required
def todo_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.completed = not todo.completed  # 完了・未完了を切り替え
        todo.save()
        return redirect('todo_list')