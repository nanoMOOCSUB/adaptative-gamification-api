# Generated by Django 3.0.8 on 2020-07-28 14:03

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200728_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='leadders',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
