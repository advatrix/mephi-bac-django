import uuid

from django.db import models
from lk_admin.settings import MAX_STR_LENGTH

# Create your models here.


class User(models.Model):
    external_id = models.UUIDField(unique=True, default=uuid.uuid4)
    username = models.CharField(unique=True, max_length=MAX_STR_LENGTH)
    first_name = models.CharField(max_length=MAX_STR_LENGTH)
    last_name = models.CharField(max_length=MAX_STR_LENGTH)
    middle_name = models.CharField(max_length=MAX_STR_LENGTH, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=MAX_STR_LENGTH)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=MAX_STR_LENGTH, null=True, blank=True)

    password = models.CharField(max_length=MAX_STR_LENGTH)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    access_token = models.TextField(db_index=True)
    access_token_expired = models.DateTimeField()
    refresh_token = models.TextField()
    refresh_token_expired = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'session'


#
# class Application(models.Model):
#
#
#
# class TargetGroup(models.Model):
#     name = models.TextField(max_length=MAX_STR_LENGTH, unique=True)
#     description = models.TextField(null=True, blank=True)
#
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'target_group'
#
#
# class UserToTargetGroup(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     target_group = models.ForeignKey(TargetGroup, on_delete=models.PROTECT)
#
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.user} - {self.target_group}'
#
#     class Meta:
#         db_table = 'user_to_target_group'
#         unique_together = ('user', 'target_group')
#
#
# class Notification(models.Model):
#     title = models.TextField()
#     text = models.TextField()
#     date = models.DateField()
#     target_groups = models.ManyToManyField(TargetGroup, through='NotificationToTargetGroup', null=True, blank=True)
#     users = models.ManyToManyField(User, through='NotificationToUser', null=True, blank=True)
#
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         db_table = 'notification'
#
#
# class NotificationToTargetGroup(models.Model):
#     notification = models.ForeignKey(Notification, on_delete=models.PROTECT)
#     target_group = models.ForeignKey(TargetGroup, on_delete=models.PROTECT)
#
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.notification}, {self.target_group}'
#
#     class Meta:
#         db_table = 'notification_to_target_group'
#         unique_together = ('notification', 'target_group')
#
#
# class NotificationToUser(models.Model):
#     notification = models.ForeignKey(Notification, on_delete=models.PROTECT)
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     is_read = models.BooleanField()
#
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.notification} - {self.user}'
#
#     class Meta:
#         db_table = 'notification_to_user'
#         unique_together = ('notification', 'user')
#
#
#
