# Generated by Django 4.0.4 on 2022-04-17 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
