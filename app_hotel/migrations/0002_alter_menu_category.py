# Generated by Django 4.2.1 on 2023-06-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
