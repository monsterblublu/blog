# Generated by Django 3.1.4 on 2021-01-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210117_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='article/thumbnail'),
        ),
    ]
