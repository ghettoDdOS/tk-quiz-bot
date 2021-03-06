# Generated by Django 3.2.12 on 2022-05-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('start', 'Приветственное сообщение'), ('parents', 'Экран для родителей'), ('kids', 'Экран для детей'), ('kids_test', 'Упражнения для детей')], max_length=50, null=True, unique=True, verbose_name='Тип сообщения')),
                ('text', models.TextField(null=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.AlterModelOptions(
            name='kidsgames',
            options={'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
    ]
