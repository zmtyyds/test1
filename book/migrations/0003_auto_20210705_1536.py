# Generated by Django 2.2.10 on 2021-07-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210705_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='publisher',
            name='contact',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]