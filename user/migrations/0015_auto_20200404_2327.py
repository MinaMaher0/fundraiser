# Generated by Django 3.0.4 on 2020-04-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_profile_is_authenticated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_birthDate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
