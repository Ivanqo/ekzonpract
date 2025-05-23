from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('editor', 'Редактор'),
        ('viewer', 'Читатель'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='viewer')

class Project(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('active', 'Активный'),
        ('completed', 'Завершен'),
    )
    
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    documents = models.JSONField(default=list)  # Хранение списка документов
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title