# Generated by Django 3.0.4 on 2020-04-03 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
