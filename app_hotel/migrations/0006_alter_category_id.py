# Generated by Django 4.2.3 on 2023-07-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hotel', '0005_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
