# Generated by Django 4.1.2 on 2022-10-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firs_name', models.CharField(max_length=120, verbose_name='User first Name')),
                ('last_name', models.CharField(max_length=120, verbose_name='User last Name')),
                ('username', models.CharField(max_length=120, verbose_name='Username')),
                ('password', models.CharField(max_length=20, verbose_name='User password')),
                ('date_of_join', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
