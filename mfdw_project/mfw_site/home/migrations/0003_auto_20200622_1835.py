# Generated by Django 2.1.15 on 2020-06-22 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200622_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='mail',
            new_name='username',
        ),
    ]
