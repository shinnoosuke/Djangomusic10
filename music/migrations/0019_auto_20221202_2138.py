# Generated by Django 3.2 on 2022-12-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0018_user_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teaching_inst',
            name='teaching_inst1',
        ),
        migrations.RemoveField(
            model_name='teaching_inst',
            name='teaching_inst2',
        ),
        migrations.RemoveField(
            model_name='teaching_inst',
            name='teaching_inst3',
        ),
        migrations.AddField(
            model_name='teaching_inst',
            name='revel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teaching_inst',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
