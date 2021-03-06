# Generated by Django 2.0 on 2020-03-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_pics',
            name='imgage_url',
        ),
        migrations.AddField(
            model_name='project_pics',
            name='image',
            field=models.ImageField(default=None, upload_to='test/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project_data',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project_data',
            name='rating',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='project_data',
            name='reports',
            field=models.IntegerField(default=0),
        ),
    ]
