# Generated by Django 2.2.1 on 2019-10-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_tiretreaddepthcheckhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiretreaddepthcheckhistory',
            name='checked_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]