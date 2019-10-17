# Generated by Django 2.2.1 on 2019-10-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleviolation',
            name='driver',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicleviolation',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleviolation',
            name='vehicle',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicleviolation',
            name='violates_on',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]