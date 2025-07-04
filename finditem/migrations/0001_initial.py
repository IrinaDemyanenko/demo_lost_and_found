# Generated by Django 5.2.3 on 2025-06-28 15:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Код категории')),
                ('name', models.CharField(max_length=200, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название станции')),
            ],
        ),
        migrations.CreateModel(
            name='FoundItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500, verbose_name='Описание вещи')),
                ('found_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата находки')),
                ('image_url', models.CharField(blank=True, max_length=500, verbose_name='Фото (url)')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finditem.category', verbose_name='Категория')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finditem.station', verbose_name='Станция')),
            ],
        ),
    ]
