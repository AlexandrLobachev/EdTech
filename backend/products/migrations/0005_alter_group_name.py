# Generated by Django 3.2.24 on 2024-03-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20240301_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Группа'),
        ),
    ]
