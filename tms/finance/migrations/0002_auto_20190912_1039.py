# Generated by Django 2.2.1 on 2019-09-12 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelcardusagehistory',
            name='oil_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Station'),
        ),
    ]
