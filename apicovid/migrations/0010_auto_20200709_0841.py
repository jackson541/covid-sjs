# Generated by Django 3.0.7 on 2020-07-09 11:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apicovid', '0009_auto_20200702_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(default=datetime.datetime(2020, 7, 9, 8, 41, 51, 776370))),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apicovid.Cidade')),
            ],
        ),
        migrations.AlterField(
            model_name='caso',
            name='boletim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apicovid.Boletim'),
        ),
    ]
