# Generated by Django 2.2.1 on 2019-10-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20191023_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='msg_type',
            field=models.PositiveIntegerField(choices=[(0, 'New Job'), (1, 'Update Job'), (2, 'Delete Job'), (3, 'Cancel Job'), (4, 'Enter station'), (5, 'Exit Station'), (6, 'Enter Blackdot'), (7, 'Exit Blackdot'), (10, 'Rest Request Notification'), (11, 'Rest Request Notification Approved'), (12, 'Rest Request Notification Declined'), (20, 'Vehicle Maintenance Notification'), (21, 'Vehicle Maintenance Notification Approved'), (22, 'Vehicle Maintenance Notification Declined'), (30, 'Parking Request Notification'), (31, 'Parking Request Notification Approved'), (32, 'Parking Request Notification Declined'), (40, 'Driver Change Notification'), (41, 'Driver Change Notification Approved'), (42, 'Driver Change Notification Declined'), (43, 'Driver Change Notification New Driver'), (50, 'Escort Change Notification'), (51, 'Escort Change Notification Approved'), (52, 'Escort Change Notification Declined'), (53, 'Escort Change Notification New Escort'), (60, 'Traffic Accident Notification')], default=0),
        ),
    ]
