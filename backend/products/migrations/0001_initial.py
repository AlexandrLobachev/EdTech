# Generated by Django 3.2.24 on 2024-03-01 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Продукт')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Стоимость')),
                ('start_date', models.DateTimeField(verbose_name='Дата и время старта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('min_qty_students', models.PositiveSmallIntegerField(verbose_name='Минимальное количество студентов в группе')),
                ('max_qty_students', models.PositiveSmallIntegerField(verbose_name='Максимальное количество студентов в группе')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Урок')),
                ('link_video', models.URLField(verbose_name='Ссылка на урок')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.course', verbose_name='Курс')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Группа')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.course', verbose_name='Курс')),
                ('student', models.ManyToManyField(related_name='Студент', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(related_name='courses', through='products.Enrollment', to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель'),
        ),
    ]
