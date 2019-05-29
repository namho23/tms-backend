# Generated by Django 2.2.1 on 2019-05-29 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('gas', 'Gas'), ('oil', 'Oil')], default='gas', max_length=10)),
                ('price', models.DecimalField(decimal_places=1, max_digits=5)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=30)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('station_type', models.CharField(choices=[('L', 'Loading Station'), ('U', 'Unloading Station'), ('Q', 'Quality Station'), ('O', 'Oil Station')], default='L', max_length=1)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('radius', models.DecimalField(decimal_places=1, max_digits=10)),
                ('product_category', models.CharField(choices=[('gas', 'Gas'), ('oil', 'Oil')], default='gas', max_length=10)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('working_time', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('average_time', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
            ],
            options={
                'unique_together': {('longitude', 'latitude')},
            },
        ),
    ]
