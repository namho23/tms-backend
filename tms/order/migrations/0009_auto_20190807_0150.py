# Generated by Django 2.2.1 on 2019-08-06 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20190807_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobstationproduct',
            name='due_time',
        ),
        migrations.AddField(
            model_name='jobstation',
            name='due_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
