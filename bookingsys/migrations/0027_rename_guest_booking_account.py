# Generated by Django 3.2 on 2022-02-11 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0026_auto_20220211_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='guest',
            new_name='account',
        ),
    ]
