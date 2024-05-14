#Source: https://stackoverflow.com/questions/37846721/django-typeerror-modelbase-object-is-not-iterable
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reputationaction',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='reputation_action'),
        ),
    ]