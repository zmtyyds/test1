# Generated by Django 2.2.10 on 2021-07-27 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0033_auto_20210727_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 27, 22, 53, 54, 321182)),
        ),
    ]
