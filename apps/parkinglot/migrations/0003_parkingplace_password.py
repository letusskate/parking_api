# Generated by Django 2.1.12 on 2023-01-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkinglot', '0002_auto_20230114_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingplace',
            name='password',
            field=models.CharField(default='123456', max_length=200),
        ),
    ]
