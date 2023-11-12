# Generated by Django 4.2.7 on 2023-11-12 08:32

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomModel',
            fields=[
                ('sid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='sid')),
                ('name', models.CharField(max_length=100, verbose_name='Название комнаты')),
                ('users', models.ManyToManyField(related_name='rooms', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
    ]
