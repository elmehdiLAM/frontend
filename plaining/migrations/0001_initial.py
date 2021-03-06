# Generated by Django 3.1.4 on 2021-01-02 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('CIN', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('numPhone', models.CharField(max_length=16)),
                ('maxHoraireMois', models.PositiveIntegerField(default=20)),
                ('maxHoraireJour', models.IntegerField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
