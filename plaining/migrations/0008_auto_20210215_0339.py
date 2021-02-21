# Generated by Django 3.1.4 on 2021-02-15 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plaining', '0007_auto_20210124_0415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deplacement',
            old_name='depenseEstimé',
            new_name='depenseEstimeJour',
        ),
        migrations.RemoveField(
            model_name='cours',
            name='description',
        ),
        migrations.RemoveField(
            model_name='person',
            name='image',
        ),
        migrations.AddField(
            model_name='cours',
            name='module',
            field=models.CharField(default='module', max_length=100),
        ),
        migrations.AddField(
            model_name='deplacement',
            name='kilometrage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cours',
            name='nombreheure',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='deplacement',
            name='date_depart',
            field=models.DateField(default=datetime.datetime(2021, 2, 15, 3, 39, 37, 863873)),
        ),
        migrations.AlterField(
            model_name='deplacement',
            name='date_retour',
            field=models.DateField(default=datetime.datetime(2021, 2, 16, 3, 39, 37, 863873)),
        ),
        migrations.AlterField(
            model_name='person',
            name='statue',
            field=models.CharField(choices=[('PES', 'PES'), ('PH', 'PH'), ('PA', 'PA'), ('MA', 'MA'), ('Assist', 'Assist'), ('AP/prep', 'AP/prep')], default='DOC', max_length=10),
        ),
    ]
