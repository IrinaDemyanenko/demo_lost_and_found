# Generated by Django 5.2.3 on 2025-06-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finditem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founditem',
            name='image_url',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Фото (url)'),
        ),
    ]
