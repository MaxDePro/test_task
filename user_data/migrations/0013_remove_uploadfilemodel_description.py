# Generated by Django 4.1.2 on 2022-10-29 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0012_alter_uploadfilemodel_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfilemodel',
            name='description',
        ),
    ]