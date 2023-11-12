from django.contrib import admin

from rooms.models.room import RoomModel


@admin.register(RoomModel)
class RoomModelAdmin(admin.ModelAdmin):
    ...