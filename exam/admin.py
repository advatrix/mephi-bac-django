from django.contrib import admin
from exam.models import *

# Register your models here.


class SubjectToExamTypeInline(admin.TabularInline):
    model = SubjectToExamType
    extra = 0


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'credits']
    inlines = SubjectToExamTypeInline,


class TutorToSubjectInline(admin.TabularInline):
    model = TutorToSubject
    extra = 0


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'occupation', 'room']
    inlines = TutorToSubjectInline,


class ExaminerInline(admin.TabularInline):
    model = Examiner
    extra = 0


class UserToExamScheduleInline(admin.TabularInline):
    model = UserToExamSchedule
    extra = 0


@admin.register(ExamSchedule)
class ExamScheduleAdmin(admin.ModelAdmin):
    list_display = ['subject_exam_type', 'start_time', 'end_time', 'description']
    inlines = UserToExamScheduleInline, ExaminerInline


class SubjectToStudyGroupInline(admin.TabularInline):
    model = SubjectToStudyGroup
    extra = 0


class UserToStudyGroupInline(admin.TabularInline):
    model = UserToStudyGroup
    extra = 0


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'study_program', 'description']
    inlines = SubjectToStudyGroupInline, UserToStudyGroupInline


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'result_points', 'absence', 'comment']


admin.site.register(ExamType)
admin.site.register(SubjectToExamType)
admin.site.register(UserToExamSchedule)
