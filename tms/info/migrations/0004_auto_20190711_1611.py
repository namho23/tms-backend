# Generated by Django 2.2.1 on 2019-07-11 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20190711_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='client',
            new_name='customer',
        ),
    ]
