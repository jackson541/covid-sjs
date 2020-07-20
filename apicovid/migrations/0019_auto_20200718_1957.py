# Generated by Django 3.0.7 on 2020-07-18 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicovid', '0018_auto_20200718_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletim',
            name='casosConfirmados',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='boletim',
            name='casosDeObito',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='boletim',
            name='casosDescartados',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='boletim',
            name='casosEmTratamento',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='boletim',
            name='casosInternados',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='boletim',
            name='casosNotificados',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='boletim',
            name='casosRecuperados',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='boletim',
            name='casosSuspeitos',
            field=models.PositiveIntegerField(),
        ),
    ]