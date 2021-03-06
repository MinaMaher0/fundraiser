# Generated by Django 3.0.4 on 2020-03-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20200319_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_data',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project_pics',
            name='image',
            field=models.ImageField(upload_to='project_images'),
        ),
    ]
