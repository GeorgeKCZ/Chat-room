from django.contrib import admin
from django.contrib.admin import ModelAdmin

from base.models import Room, Message

class MessageAdmin(ModelAdmin):
    @staticmethod
    def cleanup_body(modeladmin, request, queryset):
        queryset.update(body="--Deleted--")

    ordering = ['id']
    list_display = ['id', 'body', 'room', 'body_short']
    list_display_links = ['id', 'body_short']
    list_per_page = 20
    list_filter = ['room']
    search_fields = ['body', 'id']
    actions = ['cleanup_body']

    fieldsets = [
        (
            None,
            {
                'fields': ['body']
            }
        ),
        (
            'details',
            {
                'fields': ['room', 'created', 'update'],
                'description': 'Detailed information about room.'
            }
        ),
        (
            'User Information',
            {
                'fields': ['user']
            }
        )
    ]
    readonly_fields = ['id', 'created', 'updated']

#ListView
class RoomAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'description']
    list_display_links = ['id', 'name']
    list_per_page = 20
    search_fields = ['name', 'description']

#FornVeiw


fieldsets = [
    (
        None,
        {
            'fields': ['id', 'name', 'description']
        }
    ),
    (
        'Detail',
        {
            'fields': ['participants', 'created', 'update'],
            'description': 'Detailed information about rooms'
        }
    )
]
readonly_fields = ['id', 'created', 'update']
admin.site.register(Room)
admin.site.register(Message, MessageAdmin)
