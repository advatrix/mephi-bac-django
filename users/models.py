import uuid

from django.db import models
from lk_admin.settings import MAX_STR_LENGTH

# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(unique=True, max_length=MAX_STR_LENGTH)
    first_name = models.CharField(max_length=MAX_STR_LENGTH)
    last_name = models.CharField(max_length=MAX_STR_LENGTH)
    middle_name = models.CharField(max_length=MAX_STR_LENGTH, null=True, blank=True)
    email = models.CharField(unique=True, max_length=MAX_STR_LENGTH)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=MAX_STR_LENGTH, null=True, blank=True)

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
