# Generated by Django 5.1.4 on 2025-03-20 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('project_updated', models.DateTimeField(auto_now=True)),
                ('stars', models.IntegerField(default=0)),
                ('project_description', models.TextField(blank=True, null=True)),
                ('is_starred', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'projects',
                'managed': True,
            },
        ),
    ]
