# Generated by Django 5.1.4 on 2024-12-19 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_comments_author_alter_comments_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.article', verbose_name='Статья'),
            preserve_default=False,
        ),
    ]
