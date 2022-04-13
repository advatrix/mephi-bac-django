from django.contrib import admin
from notifications.models import *

# Register your models here.


class NotificationToNotificationGroupInline(admin.TabularInline):
    model = NotificationToNotificationGroup


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'description']
    search_fields = ['title', 'name']
    inlines = [NotificationToNotificationGroupInline]


@admin.register(NotificationGroup)
class NotificationGroupAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(UserToNotificationGroup)
class UserToNotificationGroupAdmin(admin.ModelAdmin):
    search_fields = ['notification_group__name', 'user__username']
    autocomplete_fields = ['user']
    list_filter = ['notification_group__name']


@admin.register(NotificationToUser)
class NotificationToUserAdmin(admin.ModelAdmin):
    search_fields = ['notification__title', 'user__username']
    autocomplete_fields = ['user']

