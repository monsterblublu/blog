# Generated by Django 3.1.4 on 2021-01-17 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210116_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='article',
            name='snippet',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
