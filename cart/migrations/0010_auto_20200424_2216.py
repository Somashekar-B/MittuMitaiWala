# Generated by Django 3.0.4 on 2020-04-24 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_orders_confirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='order_id',
            new_name='order',
        ),
    ]
