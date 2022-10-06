from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    text = models.TextField(blank=False)


class Message(models.Model):
    chat = models.ForeignKey(
        News,
        verbose_name='Чат под новостью',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)
