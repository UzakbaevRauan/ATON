from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_delete
from django.dispatch import receiver

User = get_user_model()

class Client(models.Model):
    account_number = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    inn = models.CharField(max_length=12)
    responsible_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    STATUS_CHOICES = (
        ('Не в работе', 'Не в работе'),
        ('В работе', 'В работе'),
        ('Отказ', 'Отказ'),
        ('Сделка закрыта', 'Сделка закрыта'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Не в работе')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

# Создаем обработчик сигнала для удаления связанных клиентов при удалении пользователя
@receiver(pre_delete, sender=User)
def delete_related_clients(sender, instance, **kwargs):
    instance.clients.all().delete()
