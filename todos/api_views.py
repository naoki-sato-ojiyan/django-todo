from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    # ログインユーザーのTodoのみ取得
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    # 作成時にログインユーザーを自動セット
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)