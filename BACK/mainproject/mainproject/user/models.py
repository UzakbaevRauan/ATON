from django.contrib.auth.models import AbstractUser, Group, Permission 
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

    class Meta:
        permissions = (
            ('can_access_admin_panel', 'Can access admin panel'),
            # Добавьте дополнительные разрешения здесь по необходимости
        )
