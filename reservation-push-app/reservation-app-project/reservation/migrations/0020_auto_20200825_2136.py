# Generated by Django 2.1.5 on 2020-08-25 12:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0019_auto_20200825_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 12, 36, 57, 720289, tzinfo=utc)),
        ),
    ]
