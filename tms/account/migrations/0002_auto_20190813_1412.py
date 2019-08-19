# Generated by Django 2.2.1 on 2019-08-13 06:12

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=20)),
                ('model_name', models.CharField(max_length=20)),
                ('actions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('permissions', models.ManyToManyField(to='account.Permission')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='permission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.UserPermission'),
        ),
    ]