# Generated by Django 4.2.1 on 2023-06-27 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_hotel', '0002_alter_menu_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(default=1, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_hotel.category'),
        ),
    ]