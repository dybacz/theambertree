# Generated by Django 3.2 on 2022-02-15 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0031_booking_booking_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='number_of_guests',
        ),
    ]
