# Generated by Django 3.1.4 on 2021-01-12 01:04

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
