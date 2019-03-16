# Generated by Django 2.1.7 on 2019-03-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0003_auto_20190316_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricity',
            name='year',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='electricity',
            name='month',
            field=models.PositiveIntegerField(),
        ),
    ]
