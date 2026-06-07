# 📝 Django ToDoアプリ

Python + Django + Docker + PostgreSQLで作ったToDoアプリです。

## 🛠 使用技術

- Python 3.14
- Django 6.0
- PostgreSQL 16
- Docker / Docker Compose
- Bootstrap 5

## ✨ 機能

- Todoの追加・削除・完了切り替え
- ユーザー認証（ログイン・ログアウト）
- ユーザーごとのTodo管理

## 🚀 起動方法

```bash
# リポジトリをクローン
git clone git@github.com:naoki-sato-ojiyan/django-todo.git
cd django-todo

# .envファイルを作成（.env.exampleを参考に）
cp .env.example .env

# Docker起動
docker compose up --build

# マイグレーション
docker compose exec web python manage.py migrate

# 管理者ユーザー作成
docker compose exec web python manage.py createsuperuser
```

## 📝 環境変数

`.env.example`を参考に`.env`ファイルを作成してください。