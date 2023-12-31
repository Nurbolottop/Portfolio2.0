# Generated by Django 4.2.7 on 2023-11-08 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_infouser_options_alter_infouser_descriptions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('age', models.CharField(max_length=3, verbose_name='Возраст')),
                ('nation', models.CharField(max_length=255, verbose_name='Нация')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('telegram', models.CharField(max_length=255, verbose_name='Username телеграм')),
                ('language', models.CharField(max_length=255, verbose_name='Знание языка')),
                ('year', models.CharField(max_length=255, verbose_name='Годы опыта')),
                ('projects', models.CharField(max_length=255, verbose_name='Завершенные проекты')),
                ('clients', models.CharField(max_length=255, verbose_name='Счастливые клиенты')),
                ('awards', models.CharField(max_length=255, verbose_name='Полученные награды')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
    ]
