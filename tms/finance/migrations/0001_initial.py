# Generated by Django 2.2.1 on 2019-06-21 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('hr', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=1, max_digits=5)),
                ('is_complete', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
        ),
        migrations.CreateModel(
            name='FuelCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_company', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100, unique=True)),
                ('key', models.CharField(max_length=100)),
                ('last_charge_date', models.DateField(blank=True, null=True)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Department')),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='finance.FuelCard')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle.Vehicle')),
            ],
            options={
                'ordering': ['-last_charge_date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ETCCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_company', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100, unique=True)),
                ('key', models.CharField(max_length=100)),
                ('last_charge_date', models.DateField(blank=True, null=True)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Department')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
            options={
                'ordering': ['-last_charge_date'],
                'abstract': False,
            },
        ),
    ]
