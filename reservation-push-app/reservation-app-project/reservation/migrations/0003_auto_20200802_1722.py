# Generated by Django 2.1.5 on 2020-08-02 08:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20200717_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 8, 22, 2, 278037, tzinfo=utc)),
        ),
    ]
