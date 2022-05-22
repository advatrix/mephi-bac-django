from django.db import models
from lk_admin.settings import MAX_STR_LENGTH
from users.models import User

from django.utils.translation import gettext_lazy as _


# Create your models here.


class ExamType(models.Model):
    name = models.CharField(max_length=MAX_STR_LENGTH, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'exam_type'
        verbose_name = _('exam type')
        verbose_name_plural = _('exam types')


class Subject(models.Model):
    name = models.CharField(max_length=MAX_STR_LENGTH, unique=True)
    credits = models.IntegerField(null=True, blank=True)
    exam_types = models.ManyToManyField(ExamType, through='SubjectToExamType')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'


class SubjectToExamType(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    exam_type = models.ForeignKey(ExamType, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.exam_type} of {self.subject}'

    class Meta:
        db_table = 'subject_to_exam_type'


class Tutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    occupation = models.TextField()
    subjects = models.ManyToManyField(Subject, through='TutorToSubject')
    personal_link = models.TextField()
    email = models.EmailField(null=True, blank=True)
    room = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'

    @property
    def full_name(self):
        return self.user

    class Meta:
        db_table = 'tutor'


class TutorToSubject(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tutor} >> {self.subject}'

    class Meta:
        db_table = 'tutor_to_subject'


class ExamSchedule(models.Model):
    subject_exam_type = models.ForeignKey(SubjectToExamType, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    registration_start_time = models.DateTimeField(null=True, blank=True)
    registration_end_time = models.DateTimeField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    room = models.TextField(null=True, blank=True)

    max_points = models.IntegerField(null=True, blank=True)
    pass_points = models.IntegerField(null=True, blank=True)

    examiners = models.ManyToManyField(Tutor, through='Examiner')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject_exam_type}: {self.start_time}'

    class Meta:
        db_table = 'exam_schedule'
        verbose_name = _('exam schedule')
        verbose_name_plural = _('exam schedule')


class Examiner(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.PROTECT)
    exam_schedule = models.ForeignKey(ExamSchedule, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tutor} on {self.exam_schedule.__str__()}'

    class Meta:
        db_table = 'examiner'


class StudyGroup(models.Model):
    name = models.CharField(max_length=MAX_STR_LENGTH, unique=True)
    study_program = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    users = models.ManyToManyField(User, through='UserToStudyGroup')
    subjects = models.ManyToManyField(Subject, through='SubjectToStudyGroup')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'study_group'


class SubjectToStudyGroup(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject} -> {self.study_group}'

    class Meta:
        db_table = 'subject_to_study_group'


class UserToStudyGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} -> {self.study_group}'

    class Meta:
        db_table = 'user_to_study_group'


class UserToExamSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    exam_schedule = models.ForeignKey(ExamSchedule, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} -> '

    class Meta:
        db_table = 'user_to_exam_schedule'


class ExamResult(models.Model):
    user_to_exam_schedule = models.OneToOneField(UserToExamSchedule, on_delete=models.PROTECT)
    result_points = models.IntegerField(null=True, blank=True)
    absence = models.BooleanField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    examiner = models.ForeignKey(Tutor, on_delete=models.PROTECT, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_to_exam_schedule

    class Meta:
        db_table = 'exam_result'
        verbose_name = _('exam result')
        verbose_name_plural = _('exam results')
