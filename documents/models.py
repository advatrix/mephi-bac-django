import uuid
from django.db import models
from lk_admin.settings import MAX_STR_LENGTH
from users.models import User
from role_model.models import Permission
# Create your models here.


class DocumentTemplate(models.Model):
    name = models.CharField(max_length=MAX_STR_LENGTH)
    template = models.TextField()
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'document_template'


class DocumentStatus(models.Model):
    name = models.CharField(max_length=MAX_STR_LENGTH, unique=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'document_status'


class Document(models.Model):
    template = models.ForeignKey(DocumentTemplate, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(DocumentStatus, on_delete=models.PROTECT)
    content = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.template} - {self.user} - {self.status}'

    class Meta:
        db_table = 'document'


class DocumentPermission(models.Model):
    name = models.CharField(max_length=MAX_STR_LENGTH, null=True, blank=True)
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)
    can_read = models.BooleanField()
    can_change_status = models.BooleanField()
    can_edit = models.BooleanField()
    description = models.TextField(null=True, blank=True)

    documents = models.ManyToManyField(Document, through='DocumentToDocumentPermission')
    template = models.ForeignKey(DocumentTemplate, null=True, blank=True, on_delete=models.PROTECT)
    is_for_all = models.BooleanField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'document_permission'


class DocumentToDocumentPermission(models.Model):
    document = models.ForeignKey(Document, on_delete=models.PROTECT)
    document_permission = models.ForeignKey(DocumentPermission, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.document} -> {self.document_permission}'

    class Meta:
        db_table = 'document_to_document_permission'


class DocumentHistory(models.Model):
    document = models.ForeignKey(Document, on_delete=models.PROTECT)
    old_status = models.ForeignKey(
        DocumentStatus, on_delete=models.PROTECT, null=True, blank=True, related_name='document_history_old_status'
    )
    new_status = models.ForeignKey(DocumentStatus, on_delete=models.PROTECT, related_name='document_history_new_status')
    comment = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    time = models.DateTimeField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.document} :: {self.old_status} -> {self.new_status} on {self.time}'

    class Meta:
        db_table = 'document_history'
