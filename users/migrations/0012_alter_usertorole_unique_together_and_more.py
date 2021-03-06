# Generated by Django 4.0.3 on 2022-04-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_notificationtotargetgroup_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usertorole',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='usertorole',
            name='role',
        ),
        migrations.RemoveField(
            model_name='usertorole',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='UserToRole',
        ),
    ]
