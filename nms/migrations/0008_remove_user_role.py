# Generated by Django 5.1.4 on 2024-12-24 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nms', '0007_note_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]