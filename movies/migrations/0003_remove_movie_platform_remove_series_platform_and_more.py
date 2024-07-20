# Generated by Django 5.0.7 on 2024-07-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_streamingplatfrom_streamingplatform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='series',
            name='platform',
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
