from django.contrib import admin

from data_sync.models import *

# Register your models here.


@admin.register(EntityTemplate)
class EntityTemplateAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'description']


@admin.register(SimpleDataTable)
class SimpleDataTableAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'integer', 'optional_string', 'float']
