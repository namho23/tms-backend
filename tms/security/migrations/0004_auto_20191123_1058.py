# Generated by Django 2.2.1 on 2019-11-23 10:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('security', '0003_auto_20191120_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='securitylearningprogram',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='test',
            name='departments',
        ),
        migrations.AddField(
            model_name='securitylearningprogram',
            name='audiences',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='test',
            name='appliants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]