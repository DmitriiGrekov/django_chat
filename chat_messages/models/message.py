from django.db import models
from django.contrib.auth.models import User

from core.mixins.sid_indexed import SidIndexedMixin

from rooms.models.room import RoomModel


class MessageModel(SidIndexedMixin, models.Model):
    """Модель сообщения."""

    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE,
                                related_name='messages', verbose_name='Комната')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='messages', verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст сообщения')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Комната: {self.room.sid} -> Пользователь: {self.user.id} -> Сообщение: {self.sid}'
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('-created_at', )