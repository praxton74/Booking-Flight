# Generated by Django 4.0.6 on 2024-02-25 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0006_rename_code_flight_num_remove_flight_exists_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='exists',
            field=models.IntegerField(default=0),
        ),
    ]
