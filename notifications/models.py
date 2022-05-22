import uuid

from django.db import models
from lk_admin.settings import MAX_STR_LENGTH

from django.utils.translation import gettext_lazy as _

from users.models import User

# Create your models here.


class NotificationGroup(models.Model):
    name = models.TextField(max_length=MAX_STR_LENGTH, unique=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'notification_group'


class UserToNotificationGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    notification_group = models.ForeignKey(NotificationGroup, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.notification_group}'

    class Meta:
        db_table = 'user_to_notification_group'
        unique_together = ('user', 'notification_group')


class Notification(models.Model):
    external_id = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=MAX_STR_LENGTH, unique=True)
    title = models.TextField()
    description = models.CharField(max_length=MAX_STR_LENGTH, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    notification_groups = models.ManyToManyField(
        NotificationGroup, through='NotificationToNotificationGroup', blank=True
    )
    users = models.ManyToManyField(User, through='NotificationToUser', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'notification'
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')



class NotificationToNotificationGroup(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.PROTECT)
    notification_group = models.ForeignKey(NotificationGroup, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.notification}, {self.notification_group}'

    class Meta:
        db_table = 'notification_to_notification_group'
        unique_together = ('notification', 'notification_group')


class NotificationToUser(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_read = models.BooleanField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.notification} - {self.user}'

    class Meta:
        db_table = 'notification_to_user'
        unique_together = ('notification', 'user')
