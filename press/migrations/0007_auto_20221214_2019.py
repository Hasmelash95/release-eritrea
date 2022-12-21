# Generated by Django 3.2.16 on 2022-12-14 20:19

import cloudinary.models
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('press', '0006_auto_20221214_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=cloudinary.models.CloudinaryField(default='temporary', max_length=255, verbose_name='image'),
        ),
    ]