# Generated by Django 3.0.4 on 2020-04-25 18:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0015_auto_20200425_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='user_display',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 18, 0, 36, 618896, tzinfo=utc)),
        ),
    ]
