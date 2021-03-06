# Generated by Django 3.2 on 2022-07-12 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0034_auto_20220710_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='timeslot',
            field=models.ManyToManyField(default='', limit_choices_to={'booking_status': 1, 'date__range': (datetime.date(2022, 7, 13), datetime.date(2022, 8, 12)), 'status': 1}, related_name='booking_table_slot', to='bookingsys.BookingSlot'),
        ),
        migrations.AlterField(
            model_name='bookingslot',
            name='booking_status',
            field=models.IntegerField(choices=[(0, 'Booked'), (1, 'Available')], default=1),
        ),
    ]
