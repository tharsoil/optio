# Generated by Django 5.1.4 on 2025-03-05 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuickNote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.TextField()),
            ],
            options={
                'db_table': 'optio_quicknotes',
            },
        ),
    ]
