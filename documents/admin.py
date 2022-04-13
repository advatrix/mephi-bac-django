from django.contrib import admin

from documents.models import *

# Register your models here.


class DocumentToDocumentPermissionInline(admin.TabularInline):
    model = DocumentToDocumentPermission
    extra = 0


@admin.register(DocumentPermission)
class DocumentPermissionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'permission', 'can_read', 'can_change_status', 'can_edit', 'is_for_all', 'description']


@admin.register(DocumentTemplate)
class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'description']
    search_fields = ['name']


@admin.register(DocumentStatus)
class DocumentStatusAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'description']
    search_fields = ['name']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    inlines = DocumentToDocumentPermissionInline,


@admin.register(DocumentHistory)
class DocumentHistoryAdmin(admin.ModelAdmin):
    pass
