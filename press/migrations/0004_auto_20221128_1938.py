# Generated by Django 3.2.16 on 2022-11-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0003_alter_comment_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=80),
        ),
    ]
