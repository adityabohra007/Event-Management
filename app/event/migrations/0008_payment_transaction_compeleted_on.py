# Generated by Django 4.0.2 on 2022-02-24 22:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_events_booking_end_alter_events_booking_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='transaction_compeleted_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 24, 22, 7, 58, 744926, tzinfo=utc)),
        ),
    ]
