# Generated by Django 4.2.3 on 2023-08-03 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='menu',
            new_name='MenuItem',
        ),
    ]
