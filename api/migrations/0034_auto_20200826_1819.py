# Generated by Django 3.0.8 on 2020-08-26 18:19

import api.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_auto_20200826_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialprofile',
            name='image',
            field=enumfields.fields.EnumField(default='user', enum=api.models.SocialProfile.AvatarType, max_length=11),
        ),
    ]
