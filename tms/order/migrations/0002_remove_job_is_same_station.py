# Generated by Django 2.2.1 on 2019-10-03 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='is_same_station',
        ),
    ]