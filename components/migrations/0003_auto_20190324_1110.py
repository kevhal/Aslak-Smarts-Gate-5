# Generated by Django 2.1.7 on 2019-03-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_component_ikea_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='type',
            field=models.CharField(choices=[('light', 'light'), ('socket', 'socket')], max_length=100),
        ),
    ]
