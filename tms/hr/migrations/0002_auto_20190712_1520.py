# Generated by Django 2.2.1 on 2019-07-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffprofile',
            name='status',
            field=models.CharField(choices=[('A', 'Available'), ('D', 'Driving'), ('N', 'Not Available')], default='A', max_length=1),
        ),
    ]