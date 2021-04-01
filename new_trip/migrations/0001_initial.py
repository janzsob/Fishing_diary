# Generated by Django 3.1.7 on 2021-04-01 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('place', models.CharField(max_length=100, verbose_name='Place')),
                ('s_date', models.DateTimeField(verbose_name='Starting Date')),
                ('e_date', models.DateTimeField(verbose_name='Ending Date')),
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trips',
            },
        ),
        migrations.CreateModel(
            name='Fisherman',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Fisherman')),
                ('fisherman_id', models.AutoField(primary_key=True, serialize=False)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_trip.trips')),
            ],
            options={
                'verbose_name': 'Fisherman',
                'verbose_name_plural': 'Fishermen',
            },
        ),
    ]