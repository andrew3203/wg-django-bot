# Generated by Django 3.2.13 on 2022-05-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_referral_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='traffic',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='referral',
            name='reward',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='peer',
            name='recived_bytes',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='peer',
            name='trancmitted_bytes',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='servertraffic',
            name='recived_bytes',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='servertraffic',
            name='trancmitted_bytes',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
