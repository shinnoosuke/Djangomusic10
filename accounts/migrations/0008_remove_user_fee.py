# Generated by Django 3.2 on 2022-11-29 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_is_musician'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fee',
        ),
    ]
