# Generated by Django 4.0.2 on 2022-02-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_payment_transaction_compeleted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='transaction_compeleted_on',
            field=models.DateTimeField(),
        ),
    ]