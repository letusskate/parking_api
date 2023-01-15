# Generated by Django 2.1.12 on 2023-01-14 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.IntegerField()),
                ('updated_at', models.IntegerField()),
                ('format_created_at', models.DateTimeField(auto_now=True)),
                ('format_updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('hourPrice', models.FloatField()),
                ('monthPrice', models.FloatField()),
                ('d', models.IntegerField()),
                ('m', models.IntegerField()),
                ('s', models.IntegerField()),
            ],
            options={
                'verbose_name': 'ParkingLot',
                'verbose_name_plural': 'ParkingLot',
                'db_table': 'ParkingLot',
            },
        ),
        migrations.CreateModel(
            name='ParkingPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.IntegerField()),
                ('updated_at', models.IntegerField()),
                ('format_created_at', models.DateTimeField(auto_now=True)),
                ('format_updated_at', models.DateTimeField(auto_now_add=True)),
                ('identifier', models.CharField(max_length=200)),
                ('spare', models.BooleanField(default=True)),
                ('parkingLot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parkingLot_parkingPlace', to='parkinglot.ParkingLot')),
            ],
            options={
                'verbose_name': 'ParkingPlace',
                'verbose_name_plural': 'ParkingPlace',
                'db_table': 'ParkingPlace',
            },
        ),
    ]
