from django.contrib import admin

from chat_messages.models.message import MessageModel


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    ...