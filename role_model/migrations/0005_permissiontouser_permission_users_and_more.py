# Generated by Django 4.0.3 on 2022-04-11 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_usertorole_unique_together_and_more'),
        ('role_model', '0004_alter_permissiontoaction_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionToUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'permission_to_user',
            },
        ),
        migrations.AddField(
            model_name='permission',
            name='users',
            field=models.ManyToManyField(through='role_model.PermissionToUser', to='users.user'),
        ),
        migrations.AddField(
            model_name='permissiontouser',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='role_model.permission'),
        ),
        migrations.AddField(
            model_name='permissiontouser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
    ]