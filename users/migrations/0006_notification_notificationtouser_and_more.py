# Generated by Django 4.0.3 on 2022-04-04 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_notificationtotargetgroup_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'notification',
            },
        ),
        migrations.CreateModel(
            name='NotificationToUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'db_table': 'notification_to_user',
                'unique_together': {('notification', 'user')},
            },
        ),
        migrations.CreateModel(
            name='NotificationToTargetGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.notification')),
                ('target_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.targetgroup')),
            ],
            options={
                'db_table': 'notification_to_target_group',
                'unique_together': {('notification', 'target_group')},
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='target_groups',
            field=models.ManyToManyField(blank=True, null=True, through='users.NotificationToTargetGroup', to='users.targetgroup'),
        ),
        migrations.AddField(
            model_name='notification',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, through='users.NotificationToUser', to='users.user'),
        ),
    ]