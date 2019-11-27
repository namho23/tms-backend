# Generated by Django 2.2.1 on 2019-11-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0009_auto_20191120_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g7mqttevent',
            name='end_lat',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='g7mqttevent',
            name='end_lng',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='g7mqttevent',
            name='start_lat',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='g7mqttevent',
            name='start_lng',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
    ]
