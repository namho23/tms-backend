# Generated by Django 2.2.1 on 2019-08-09 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20190809_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelcard',
            name='master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='finance.FuelCard'),
        ),
    ]