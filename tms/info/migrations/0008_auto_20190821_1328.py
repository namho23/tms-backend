# Generated by Django 2.2.1 on 2019-08-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20190813_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='customers',
            field=models.ManyToManyField(related_name='stations', to='hr.CustomerProfile'),
        ),
    ]