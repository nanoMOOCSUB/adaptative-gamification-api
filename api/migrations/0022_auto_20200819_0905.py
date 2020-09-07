# Generated by Django 3.0.8 on 2020-08-19 09:05

import api.models
import django.core.validators
from django.db import migrations, models
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200818_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developmenttool',
            name='length',
        ),
        migrations.RemoveField(
            model_name='developmenttool',
            name='sort_by',
        ),
        migrations.RemoveField(
            model_name='developmenttool',
            name='users',
        ),
        migrations.AddField(
            model_name='developmenttool',
            name='attempts',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='developmenttool',
            name='mechanic_class',
            field=enumfields.fields.EnumField(default='Badge', enum=api.models.DevelopmentTool.Mechanic, max_length=10),
        ),
    ]