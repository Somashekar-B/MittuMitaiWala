# Generated by Django 3.0.4 on 2020-04-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20200424_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='order_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='order_id',
            field=models.BigIntegerField(null=True),
        ),
    ]