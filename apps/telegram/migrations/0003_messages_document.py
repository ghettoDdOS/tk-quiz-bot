# Generated by Django 3.2.12 on 2022-05-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_auto_20220519_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='telegram/tests', verbose_name='Файл с упражнениями'),
        ),
    ]
