# Generated by Django 4.2.1 on 2024-05-02 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataloger_app', '0002_alter_data_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='humidity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='temprature',
            field=models.FloatField(null=True),
        ),
    ]