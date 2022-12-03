# Generated by Django 3.2 on 2022-12-03 08:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0020_auto_20221203_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.URLField(blank=True, null=True)),
                ('fee', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('academic', models.TextField(max_length=500)),
                ('experience', models.TextField(max_length=500)),
                ('certificate', models.TextField(max_length=500)),
                ('message', models.TextField(max_length=500)),
                ('oneword', models.TextField(max_length=500)),
            ],
        ),
    ]
