# Generated by Django 2.2.10 on 2021-07-27 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0028_auto_20210727_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 27, 22, 36, 49, 390642)),
        ),
    ]