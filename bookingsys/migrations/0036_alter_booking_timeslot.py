# Generated by Django 3.2 on 2022-07-16 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0035_auto_20220713_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='timeslot',
            field=models.ManyToManyField(default='', limit_choices_to={'booking_status': 1, 'date__range': (datetime.date(2022, 7, 16), datetime.date(2022, 8, 15)), 'status': 1}, related_name='booking_table_slot', to='bookingsys.BookingSlot'),
        ),
    ]
