# Generated by Django 4.0.3 on 2022-04-11 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('role_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'action',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='PermissionToRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='role_model.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='role_model.role')),
            ],
            options={
                'db_table': 'permission_to_role',
            },
        ),
        migrations.CreateModel(
            name='PermissionToAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='role_model.action')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='role_model.permission')),
            ],
        ),
        migrations.AddField(
            model_name='permission',
            name='actions',
            field=models.ManyToManyField(through='role_model.PermissionToAction', to='role_model.action'),
        ),
        migrations.AddField(
            model_name='permission',
            name='roles',
            field=models.ManyToManyField(through='role_model.PermissionToRole', to='role_model.role'),
        ),
    ]
