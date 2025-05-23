from rest_framework import permissions

class IsEditorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Чтение разрешено всем аутентифицированным пользователям
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Запись разрешена только редакторам
        return request.user.role == 'editor'