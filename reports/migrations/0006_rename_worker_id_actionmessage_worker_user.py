# Generated by Django 4.2.18 on 2025-01-18 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_actionmessage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actionmessage',
            old_name='worker_id',
            new_name='worker_user',
        ),
    ]
