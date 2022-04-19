# Generated by Django 4.0.3 on 2022-04-19 17:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data_sync', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleDataTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('integer', models.IntegerField()),
                ('optional_string', models.TextField(blank=True, null=True)),
                ('float', models.FloatField()),
            ],
            options={
                'db_table': 'simple_data_table',
            },
        ),
    ]