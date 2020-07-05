# Generated by Django 3.0.8 on 2020-07-05 22:08

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_remove_image_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-name']},
        ),
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=tinymce.models.HTMLField(),
        ),
    ]
