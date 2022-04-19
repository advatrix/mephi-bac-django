from django.db import models
import uuid

from lk_admin.settings import MAX_STR_LENGTH
# Create your models here.


class EntityTemplate(models.Model):
    name = models.CharField(max_length=MAX_STR_LENGTH, unique=True)
    template = models.TextField()
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'entity_template'


class SimpleDataTable(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=MAX_STR_LENGTH, unique=True)
    integer = models.IntegerField()
    optional_string = models.TextField(null=True, blank=True)
    float = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'simple_data_table'


class ExternalApplicationToken(models.Model):
    application = models.CharField(max_length=MAX_STR_LENGTH, unique=True)
    description = models.TextField(null=True, blank=True)
    token = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.application

    class Meta:
        db_table = 'external_application_token'
