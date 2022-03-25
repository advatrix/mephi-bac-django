from django.contrib import admin

from users.models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']


class SessionAdmin(admin.ModelAdmin):
    search_fields = ['username']


admin.site.register(User, UserAdmin)
admin.site.register(Session, SessionAdmin)