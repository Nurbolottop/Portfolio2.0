# Generated by Django 4.2.7 on 2023-11-07 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infouser',
            options={'verbose_name': 'Информация пользователя', 'verbose_name_plural': 'Информации пользователей'},
        ),
        migrations.AlterField(
            model_name='infouser',
            name='descriptions',
            field=models.TextField(verbose_name='Введите биографию'),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='image',
            field=models.ImageField(upload_to='image_user/', verbose_name='Загрузите фотографию'),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Введите ФИО'),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='work',
            field=models.CharField(max_length=50, verbose_name='Вввдите профессию'),
        ),
    ]
