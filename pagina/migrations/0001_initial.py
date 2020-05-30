# Generated by Django 3.0.6 on 2020-05-25 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='casos',
            fields=[
                ('data', models.DateField(primary_key=True, serialize=False)),
                ('confirmados', models.IntegerField()),
                ('recuperados', models.IntegerField()),
                ('suspeitos', models.IntegerField()),
                ('descartados', models.IntegerField()),
                ('obitos', models.IntegerField()),
            ],
        ),
    ]