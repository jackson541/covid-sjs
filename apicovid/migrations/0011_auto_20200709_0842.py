# Generated by Django 3.0.7 on 2020-07-09 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicovid', '0010_auto_20200709_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletim',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 8, 41, 59, 726825)),
        ),
    ]
