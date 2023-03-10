# Generated by Django 4.1.5 on 2023-01-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_quality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwairModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=125)),
                ('score', models.FloatField()),
                ('temp', models.FloatField()),
                ('humid', models.FloatField()),
                ('co2', models.FloatField()),
                ('voc', models.FloatField()),
                ('pm25', models.FloatField()),
            ],
        ),
    ]
