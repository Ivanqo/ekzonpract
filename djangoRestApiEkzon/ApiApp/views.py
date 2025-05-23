from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsEditorOrReadOnly

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsEditorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)