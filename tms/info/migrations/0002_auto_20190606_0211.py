# Generated by Django 2.2.1 on 2019-06-06 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='radius',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_type',
            field=models.CharField(choices=[('L', '装货地'), ('U', '卸货地'), ('Q', '质检点'), ('O', '合作油站')], default='L', max_length=1),
        ),
    ]
