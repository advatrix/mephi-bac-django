# Generated by Django 4.0.3 on 2022-04-11 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('role_model', '0003_permission_description'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='permissiontoaction',
            table='permission_to_action',
        ),
    ]
