# Generated by Django 3.0.5 on 2020-04-28 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyLessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('school', models.CharField(max_length=100, verbose_name='Организация')),
                ('annotation', models.TextField(verbose_name='Аннотация')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
