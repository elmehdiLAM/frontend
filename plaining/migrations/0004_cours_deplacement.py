# Generated by Django 3.1.4 on 2021-01-03 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plaining', '0003_person_sexe'),
    ]

    operations = [
        migrations.CreateModel(
            name='deplacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_deplacement', models.TextField(choices=[('NAT', 'National'), ('INT', 'International')], default='NAT', max_length=100)),
                ('periode', models.DurationField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plaining.person')),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etablisement', models.TextField(default='FSR', max_length=100)),
                ('date', models.DateField()),
                ('nombreheure', models.PositiveIntegerField(default=2)),
                ('date_ajout', models.TimeField(auto_now=True)),
                ('description', models.TextField(max_length=250)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plaining.person')),
            ],
        ),
    ]
