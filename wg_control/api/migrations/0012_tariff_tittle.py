# Generated by Django 3.2.13 on 2022-05-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_tariff_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='tittle',
            field=models.CharField(default='Tariff', max_length=100),
        ),
    ]
