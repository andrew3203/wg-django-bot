# Generated by Django 4.0.4 on 2022-04-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_user_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='finish_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid_at',
            field=models.DateTimeField(blank=True),
        ),
    ]