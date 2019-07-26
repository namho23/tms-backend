# Generated by Django 2.2.1 on 2019-07-26 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('unit_price', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('loading_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_as_loading_station', to='info.Station')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Product')),
                ('quality_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_as_quality_station', to='info.Station')),
            ],
            options={
                'ordering': ('-updated',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderCartUnloadingStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderCart')),
                ('unloading_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Station')),
            ],
        ),
        migrations.AddField(
            model_name='ordercart',
            name='unloading_stations',
            field=models.ManyToManyField(through='order.OrderCartUnloadingStation', to='info.Station'),
        ),
    ]
