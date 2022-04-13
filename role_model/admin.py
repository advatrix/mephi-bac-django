from django.contrib import admin
from role_model.models import *
from documents.models import DocumentPermission

# Register your models here.


class DocumentPermissionInline(admin.TabularInline):
    model = DocumentPermission
    extra = 0


class PermissionToRoleInline(admin.TabularInline):
    model = PermissionToRole
    extra = 0


class PermissionToActionInline(admin.TabularInline):
    model = PermissionToAction
    extra = 0


class PermissionToUserInline(admin.TabularInline):
    model = PermissionToUser
    extra = 0


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = PermissionToRoleInline,
    list_display = ['__str__', 'description']


@admin.register(UserToRole)
class UserToRoleAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'role__name']
    autocomplete_fields = ['user']


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    search_fields = ['url']


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = (PermissionToRoleInline, PermissionToUserInline, PermissionToActionInline, DocumentPermissionInline)
    list_display = ['__str__', 'description']
