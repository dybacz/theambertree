# Generated by Django 3.2 on 2022-02-09 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0015_alter_bookingslot_time_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='endTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='startTime',
            field=models.TimeField(),
        ),
    ]