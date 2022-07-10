# Generated by Django 3.2 on 2022-07-10 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0033_auto_20220710_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingslot',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timeslot', to='bookingsys.table'),
        ),
        migrations.AlterField(
            model_name='bookingslot',
            name='time_slot',
            field=models.ForeignKey(default='', limit_choices_to={'status': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='bookingslot', to='bookingsys.timeslot'),
        ),
    ]
