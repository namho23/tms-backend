# Generated by Django 2.2.1 on 2019-08-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_auto_20190817_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleafterdrivingcheckhistory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicleafterdrivingcheckhistory',
            name='problems',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehicledrivingcheckhistory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicledrivingcheckhistory',
            name='problems',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
