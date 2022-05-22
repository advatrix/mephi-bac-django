# Generated by Django 4.0.3 on 2022-04-20 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0012_alter_usertorole_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examiner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'examiner',
            },
        ),
        migrations.CreateModel(
            name='ExamSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('registration_start_time', models.DateTimeField(blank=True, null=True)),
                ('registration_end_time', models.DateTimeField(blank=True, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('room', models.TextField(blank=True, null=True)),
                ('max_points', models.IntegerField(blank=True, null=True)),
                ('pass_points', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('examiners', models.ManyToManyField(through='exam.Examiner', to='users.user')),
            ],
            options={
                'db_table': 'exam_schedule',
            },
        ),
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'exam_type',
            },
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('study_program', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'study_group',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('credits', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('exam_types', models.ManyToManyField(to='exam.examtype')),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.TextField()),
                ('personal_link', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('room', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tutor',
            },
        ),
        migrations.CreateModel(
            name='UserToStudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.studygroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'db_table': 'user_to_study_group',
            },
        ),
        migrations.CreateModel(
            name='UserToExamSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('exam_schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.examschedule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'db_table': 'user_to_exam_schedule',
            },
        ),
        migrations.CreateModel(
            name='TutorToSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.subject')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.tutor')),
            ],
            options={
                'db_table': 'tutor_to_subject',
            },
        ),
        migrations.AddField(
            model_name='tutor',
            name='subjects',
            field=models.ManyToManyField(through='exam.TutorToSubject', to='exam.subject'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
        migrations.CreateModel(
            name='SubjectToStudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.studygroup')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.subject')),
            ],
            options={
                'db_table': 'subject_to_study_group',
            },
        ),
        migrations.CreateModel(
            name='SubjectToExamType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('exam_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.examtype')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.subject')),
            ],
            options={
                'db_table': 'subject_to_exam_type',
            },
        ),
        migrations.AddField(
            model_name='studygroup',
            name='subjects',
            field=models.ManyToManyField(through='exam.SubjectToStudyGroup', to='exam.subject'),
        ),
        migrations.AddField(
            model_name='studygroup',
            name='users',
            field=models.ManyToManyField(through='exam.UserToStudyGroup', to='users.user'),
        ),
        migrations.AddField(
            model_name='examschedule',
            name='subject_exam_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.subjecttoexamtype'),
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_points', models.IntegerField(blank=True, null=True)),
                ('absence', models.BooleanField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user_to_exam_schedule', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='exam.usertoexamschedule')),
            ],
            options={
                'db_table': 'exam_result',
            },
        ),
        migrations.AddField(
            model_name='examiner',
            name='exam_schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.examschedule'),
        ),
        migrations.AddField(
            model_name='examiner',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
    ]