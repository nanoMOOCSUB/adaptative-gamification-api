# Generated by Django 3.0.8 on 2020-08-17 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_unlockable_locked_html'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='sort_by',
            new_name='by',
        ),
        migrations.RenameField(
            model_name='level',
            old_name='length',
            new_name='max_value',
        ),
        migrations.RemoveField(
            model_name='level',
            name='users',
        ),
        migrations.AddField(
            model_name='level',
            name='value',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
