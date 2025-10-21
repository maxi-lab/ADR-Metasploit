from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        # Build the cmd field as required
        safe_desc = task.description 
        cmd_text = f'echo "Nueva tarea: {safe_desc}" >> /tmp/task_log.txt'
        task.cmd = cmd_text
        # Execute via os.system as requested
        try:
            import os
            os.system(cmd_text)
        except Exception:
            # Ignore execution errors but keep cmd stored
            pass
        task.save()

class PingView(APIView):
    def get(self, request):
        return Response({'ping': 'pong'})
