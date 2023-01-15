# Generated by Django 2.1.12 on 2023-01-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='parkingEndTime',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='parkingBeginTime',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]