# Generated by Django 2.2.1 on 2019-11-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_job_total_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobstationproduct',
            name='volume',
        ),
        migrations.AddField(
            model_name='qualitycheck',
            name='volume',
            field=models.FloatField(default=0),
        ),
    ]