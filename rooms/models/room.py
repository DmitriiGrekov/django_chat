from django.db import models
from django.contrib.auth.models import User
from core.mixins.sid_indexed import SidIndexedMixin


class RoomModel(SidIndexedMixin, models.Model):
    """Модель комнаты."""

    name = models.CharField('Название комнаты', max_length=100)

    users = models.ManyToManyField(User, verbose_name='Пользователи', related_name='rooms')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'