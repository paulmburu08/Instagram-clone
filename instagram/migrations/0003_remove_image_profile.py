# Generated by Django 3.0.8 on 2020-07-05 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20200705_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]
