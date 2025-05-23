from rest_framework import serializers
from .models import Project, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'status', 'documents', 'created_at', 'updated_at', 'created_by']
    
    def validate_documents(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Documents must be a list")
        return value