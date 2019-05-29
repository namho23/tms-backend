# Generated by Django 2.2.1 on 2019-05-29 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('vehicle', '0001_initial'),
        ('road', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.PositiveIntegerField(choices=[(0, 'Job Progress - Not Started'), (1, 'Job Progress - Completed'), (2, 'Job Progress - To Loading Station'), (3, 'Job Progress - Arrived at Loading Station'), (4, 'Job Progress - Loading at Loading Station'), (5, 'Job Progress - Finish Loading at Loading Station'), (6, 'Job Progress - To Quality Station'), (7, 'Job Progress - Arrived at Quality Station'), (8, 'Job Progress - Checking at Quality Station'), (9, 'Job Progress - Finish Checking at Quality Station'), (10, 'Job Progress - To Unloading Station'), (11, 'Job Progress - Arrived at Unloading Station'), (12, 'Job Progress - Unloading at Unloading Station'), (13, 'Job Progress - Finish Unloading Station')], default=0)),
                ('start_due_time', models.DateTimeField(blank=True, null=True)),
                ('finish_due_time', models.DateTimeField(blank=True, null=True)),
                ('started_on', models.DateTimeField(blank=True, null=True)),
                ('arrived_loading_station_on', models.DateTimeField(blank=True, null=True)),
                ('started_loading_on', models.DateTimeField(blank=True, null=True)),
                ('finished_loading_on', models.DateTimeField(blank=True, null=True)),
                ('departure_loading_station_on', models.DateTimeField(blank=True, null=True)),
                ('arrived_quality_station_on', models.DateTimeField(blank=True, null=True)),
                ('started_checking_on', models.DateTimeField(blank=True, null=True)),
                ('finished_checking_on', models.DateTimeField(blank=True, null=True)),
                ('departure_quality_station_on', models.DateTimeField(blank=True, null=True)),
                ('finished_on', models.DateTimeField(blank=True, null=True)),
                ('total_weight', models.PositiveIntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='account.DriverProfile')),
                ('escort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='account.EscortProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.PositiveIntegerField()),
                ('mission_weight', models.PositiveIntegerField(blank=True, null=True)),
                ('loading_weight', models.PositiveIntegerField(blank=True, null=True)),
                ('unloading_weight', models.PositiveIntegerField(blank=True, null=True)),
                ('arrived_station_on', models.DateTimeField(blank=True, null=True)),
                ('started_unloading_on', models.DateTimeField(blank=True, null=True)),
                ('finished_unloading_on', models.DateTimeField(blank=True, null=True)),
                ('departure_station_on', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Job')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderProductDeliver')),
            ],
            options={
                'ordering': ['step'],
            },
        ),
        migrations.CreateModel(
            name='JobBillDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('O', 'Bill from Oil Station'), ('L', 'Bill from Loading Station'), ('U', 'Bill from UnLoading Station'), ('Q', 'Bill from Quality Station')], default='L', max_length=1)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='job.Job')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='missions',
            field=models.ManyToManyField(through='job.Mission', to='order.OrderProductDeliver'),
        ),
        migrations.AddField(
            model_name='job',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
        migrations.AddField(
            model_name='job',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='road.Route'),
        ),
        migrations.AddField(
            model_name='job',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='vehicle.Vehicle'),
        ),
        migrations.CreateModel(
            name='DriverNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='account.DriverProfile')),
            ],
        ),
    ]
