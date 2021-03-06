# Generated by Django 3.1.4 on 2021-01-24 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plaining', '0004_cours_deplacement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deplacement',
            name='periode',
        ),
        migrations.AddField(
            model_name='deplacement',
            name='date_depart',
            field=models.DateField(default=datetime.datetime(2021, 1, 24, 3, 40, 37, 846482)),
        ),
        migrations.AddField(
            model_name='deplacement',
            name='date_retour',
            field=models.DateField(default=datetime.datetime(2021, 1, 25, 3, 40, 37, 846482)),
        ),
        migrations.AddField(
            model_name='deplacement',
            name='self_veicule',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cours',
            name='etablisement',
            field=models.CharField(default='FSR', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='maxHoraireJour',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
