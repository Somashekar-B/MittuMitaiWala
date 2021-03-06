# Generated by Django 3.0.4 on 2020-04-28 16:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0028_auto_20200428_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 16, 41, 45, 296100, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 16, 41, 45, 298094, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivered_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 16, 41, 45, 299091, tzinfo=utc)),
        ),
    ]
