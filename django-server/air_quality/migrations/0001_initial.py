# Generated by Django 4.1.5 on 2023-01-11 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AwairDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=125)),
                ('score', models.FloatField()),
                ('dew_point', models.FloatField()),
                ('temp', models.FloatField()),
                ('humid', models.FloatField()),
                ('abs_humid', models.FloatField()),
                ('co2', models.FloatField()),
                ('co2_est', models.FloatField()),
                ('co2_est_baseline', models.FloatField()),
                ('voc', models.FloatField()),
                ('voc_baseline', models.FloatField()),
                ('voc_h2_raw', models.FloatField()),
                ('voc_ethanol_raw', models.FloatField()),
                ('pm25', models.FloatField()),
                ('pm10_est', models.FloatField()),
            ],
        ),
    ]
