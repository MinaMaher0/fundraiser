# Generated by Django 3.0.4 on 2020-04-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20200404_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
