# Generated by Django 3.0.4 on 2020-04-28 16:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SweetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sweet_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='Sweet_Types')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'unique_together': {('sweet_name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='SweetCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('slugg', models.SlugField(unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='Sweet_Category')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'unique_together': {('category_name', 'slugg')},
            },
        ),
        migrations.CreateModel(
            name='OilTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oil_name', models.CharField(max_length=200)),
                ('add_on_per_kilo', models.FloatField()),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='OilTypes')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'unique_together': {('oil_name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='GheeTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ghee_name', models.CharField(max_length=200)),
                ('add_on_per_kilo', models.FloatField()),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='GheeTypes')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'unique_together': {('ghee_name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='SpecificTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200)),
                ('base_price_per_kilo', models.FloatField()),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='Sweets')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('sweet_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.SweetType')),
            ],
            options={
                'unique_together': {('type_name', 'slug')},
            },
        ),
    ]