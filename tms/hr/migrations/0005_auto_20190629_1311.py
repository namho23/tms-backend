# Generated by Django 2.2.1 on 2019-06-29 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_auto_20190627_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffprofile',
            options={'ordering': ('-updated',)},
        ),
    ]
