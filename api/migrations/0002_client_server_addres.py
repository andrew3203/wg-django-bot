# Generated by Django 3.2.13 on 2022-04-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='server_addres',
            field=models.CharField(blank=True, max_length=7),
        ),
    ]