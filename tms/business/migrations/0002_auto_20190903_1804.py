# Generated by Django 2.2.1 on 2019-09-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestapprover',
            options={'ordering': ['request', 'step']},
        ),
        migrations.AlterField(
            model_name='basicrequest',
            name='approved',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]