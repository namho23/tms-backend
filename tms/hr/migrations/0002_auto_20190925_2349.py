# Generated by Django 2.2.1 on 2019-09-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='mobile',
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='contacts',
            field=models.ManyToManyField(to='hr.CustomerContact'),
        ),
    ]