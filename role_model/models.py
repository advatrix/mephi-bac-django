# import uuid
from django.db import models

from users.models import User

from lk_admin.settings import MAX_STR_LENGTH


# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=MAX_STR_LENGTH, unique=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'role'


class UserToRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.role}'

    class Meta:
        db_table = 'user_to_role'
        unique_together = ('user', 'role')


class Action(models.Model):
    url = models.CharField(max_length=MAX_STR_LENGTH, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'action'


class Permission(models.Model):
    name = models.CharField(max_length=MAX_STR_LENGTH, unique=True)
    description = models.TextField(null=True, blank=True)
    roles = models.ManyToManyField(Role, through='PermissionToRole')
    actions = models.ManyToManyField(Action, through='PermissionToAction')
    users = models.ManyToManyField(User, through='PermissionToUser')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'permission'


class PermissionToRole(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.role} - {self.permission}'

    class Meta:
        db_table = 'permission_to_role'


class PermissionToAction(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.permission} - {self.action}'

    class Meta:
        db_table = 'permission_to_action'


class PermissionToUser(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.permission} - {self.user}'

    class Meta:
        db_table = 'permission_to_user'
