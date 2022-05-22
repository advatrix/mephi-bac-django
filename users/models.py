import uuid

from django.db import models
from lk_admin.settings import MAX_STR_LENGTH
from django.utils.translation import gettext_lazy as _

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
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.TextField(db_index=True)
    access_token_expired = models.DateTimeField()
    refresh_token = models.TextField()
    refresh_token_expired = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'session'

