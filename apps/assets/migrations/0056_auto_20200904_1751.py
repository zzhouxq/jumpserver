# Generated by Django 2.2.13 on 2020-09-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0055_auto_20200811_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='assets_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='parent_key',
            field=models.CharField(db_index=True, default='', max_length=64, verbose_name='Parent key'),
        ),
    ]
