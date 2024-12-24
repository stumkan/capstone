# Generated by Django 5.1.4 on 2024-12-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nms', '0003_ticketstatus_remove_ticket_resolved_ticket_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='status',
        ),
        migrations.AddField(
            model_name='ticket',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='TicketStatus',
        ),
    ]