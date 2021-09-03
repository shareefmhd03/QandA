from chat.models import Thread
from django.contrib import admin
from .models import ChatMessage

# Register your models here.
# class ThreadAdmin(admin.ModelAdmin):
#     inlines = [ChatMessage]
#     class Meta:
#         model = Thread


admin.site.register(Thread)

admin.site.register(ChatMessage)


# class ChatMessage(admin.TabularInline):
#     model = ChatMessage
