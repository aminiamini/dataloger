# Generated by Django 4.2.1 on 2024-05-01 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataloger_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
