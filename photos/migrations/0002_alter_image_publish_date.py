# Generated by Django 3.2 on 2021-04-08 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 16, 6, 22, 205028)),
        ),
    ]
