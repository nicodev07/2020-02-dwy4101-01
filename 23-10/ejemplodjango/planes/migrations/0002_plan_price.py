# Generated by Django 3.1.2 on 2020-10-23 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
