# Generated by Django 3.1.7 on 2021-03-31 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='date',
        ),
    ]