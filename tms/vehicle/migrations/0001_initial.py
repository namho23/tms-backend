# Generated by Django 2.2.1 on 2019-05-22 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('model', models.CharField(choices=[('T', 'Truck'), ('S', 'Semi-trailer')], default='T', max_length=1)),
                ('plate_num', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=100)),
                ('brand', models.CharField(choices=[('T', 'Tonghua'), ('L', 'Liberation'), ('Y', 'Yangzhou')], default='T', max_length=1)),
                ('load', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('document_type', models.CharField(choices=[('1', 'D1'), ('2', 'D2')], default='1', max_length=1)),
                ('authority', models.CharField(blank=True, max_length=100, null=True)),
                ('registered_on', models.DateField()),
                ('expires_on', models.DateField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
        ),
    ]
