# Generated by Django 4.1.2 on 2022-10-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0008_alter_users_first_name_alter_users_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='file_input',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]