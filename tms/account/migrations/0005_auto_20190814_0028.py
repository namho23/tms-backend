# Generated by Django 2.2.1 on 2019-08-13 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userpermission_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='app_name',
            new_name='page',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='model_name',
        ),
    ]