# Generated by Django 4.0.1 on 2022-02-01 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='manage',
        ),
    ]
