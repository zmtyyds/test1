# Generated by Django 2.2.10 on 2021-07-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_auto_20210726_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='operation_type',
            field=models.CharField(choices=[('success', 'Create'), ('warning', 'Update'), ('danger', 'Delete')], default='success', max_length=20),
        ),
    ]