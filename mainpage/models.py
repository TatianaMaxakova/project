from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Service(models.Model):
    name = models.CharField(max_length=100)  # Название услуги
    description = models.TextField()           # Описание услуги
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена услуги  либо Number
    duration = models.PositiveIntegerField()   # Продолжительность услуги в минутах
  
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('completed', 'Завершено'),
        ('canceled', 'Отменено'),
    ]
    
class Visit(models.Model):
    customer = models.ForeignKey(User, related_name='visits', on_delete=models.CASCADE, null=True, blank=True)
    executor = models.ForeignKey(User, related_name='executed_visits', on_delete=models.CASCADE, null=True, blank=True)
    given = models.DateTimeField(default=datetime.now)
    start_time = models.DateTimeField(null=True, blank=True)  # Время начала визита
    end_time = models.DateTimeField(null=True, blank=True)    # Время окончания визита
    description = models.CharField(max_length=512)  # Описание услуги или пожелания клиента
    done = models.BooleanField(default=False)  # Статус выполнения услуги
    #service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='manicure')  # Тип услуги
    color = models.CharField(max_length=7, default="#ff0000")  # Цвет в формате HEX
    notes = models.TextField(null=True, blank=True)  # Дополнительные заметки о визите
               