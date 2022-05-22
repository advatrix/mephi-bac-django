# import django.forms.models
from django.contrib import admin
# from django.db import connection

from users.models import *
from notifications.models import UserToNotificationGroup
from role_model.models import UserToRole
from role_model.admin import PermissionToUserInline
from exam.admin import UserToStudyGroupInline

# Register your models here.


class UserToNotificationGroupInline(admin.TabularInline):
    model = UserToNotificationGroup
    extra = 0


class UserToRoleInline(admin.TabularInline):
    model = UserToRole
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    inlines = (UserToNotificationGroupInline, UserToRoleInline, PermissionToUserInline, UserToStudyGroupInline)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    search_fields = ['username']


#
# @admin.register(TargetGroup)
# class TargetGroupAdmin(admin.ModelAdmin):
#     search_fields = ['name']
#
#
# @admin.register(UserToTargetGroup)
# class UserToTargetGroup(admin.ModelAdmin):
#     search_fields = ['target_group__name', 'user__username']
#     autocomplete_fields = ['user']
#     list_filter = ['target_group__name']
#
#
# @admin.register(NotificationToUser)
# class NotificationToUserAdmin(admin.ModelAdmin):
#     search_fields = ['notification__title', 'user__username']
#     autocomplete_fields = ['user']
#
#
# class NotificationToTargetGroupInlineFormset(django.forms.models.BaseInlineFormSet):
#     def save_new_objects(self, commit=True):
#         saved_objects = super(NotificationToTargetGroupInlineFormset, self).save_new_objects(commit)
#         if commit:
#             for nttg in saved_objects:
#                 query = f'''
#                     insert into "notification_to_user" (
#                         is_read,
#                         created,
#                         updated,
#                         notification_id,
#                         user_id
#                     )
#                     select
#                         false,
#                         now(),
#                         now(),
#                         {nttg.notification.id},
#                         user_id
#                     from user_to_target_group uttg
#                     where target_group_id = {nttg.target_group.id}
#                     on conflict do nothing
#                 '''
#
#                 with connection.cursor() as cursor:
#                     cursor.execute(query)
#         return saved_objects
#
#     def delete_existing(self, obj, commit=True):
#         if commit:
#             NotificationToUser.objects.filter(
#                 notification=obj.notification,
#                 user_id__in=UserToTargetGroup.objects.filter(target_group=obj.target_group).values_list('user_id',
#                                                                                                          flat=True)
#             ).delete()
#         super(NotificationToTargetGroupInlineFormset, self).delete_existing(obj, commit)
#
#
# class NotificationToTargetGroupInline(admin.TabularInline):
#     model = NotificationToTargetGroup
#     formset = NotificationToTargetGroupInlineFormset
#
#
# @admin.register(Notification)
# class NotificationAdmin(admin.ModelAdmin):
#     search_fields = ['title']
#     inlines = [NotificationToTargetGroupInline]
