# Generated by Django 4.1.2 on 2023-06-12 09:33

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='mov_cat',
            field=django_mysql.models.ListCharField(models.CharField(max_length=20), max_length=120, size=3),
        ),
    ]