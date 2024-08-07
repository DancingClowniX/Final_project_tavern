# Generated by Django 5.0.4 on 2024-05-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu/image', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='text',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
