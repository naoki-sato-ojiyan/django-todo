import pytest
from django.contrib.auth.models import User
from .models import Todo


# テスト用のユーザーを作成するフィクスチャ
@pytest.fixture
def user(db):
    return User.objects.create_user(
        username='testuser',
        password='testpass123'
    )


# テスト用のTodoを作成するフィクスチャ
@pytest.fixture
def todo(db, user):
    return Todo.objects.create(
        user=user,
        title='テストTodo',
        completed=False
    )


# Todoが正しく作成されるかテスト
def test_todo_create(todo):
    assert todo.title == 'テストTodo'
    assert todo.completed == False


# Todoの完了切り替えをテスト
def test_todo_complete(todo):
    todo.completed = not todo.completed
    todo.save()
    assert todo.completed == True


# Todoの削除をテスト
def test_todo_delete(todo):
    todo_id = todo.id
    todo.delete()
    assert Todo.objects.filter(id=todo_id).count() == 0


# ユーザーごとのTodo管理をテスト
def test_todo_user_isolation(db, user):
    other_user = User.objects.create_user(
        username='otheruser',
        password='testpass123'
    )
    Todo.objects.create(user=user, title='自分のTodo')
    Todo.objects.create(user=other_user, title='他人のTodo')

    my_todos = Todo.objects.filter(user=user)
    assert my_todos.count() == 1
    assert my_todos.first().title == '自分のTodo'