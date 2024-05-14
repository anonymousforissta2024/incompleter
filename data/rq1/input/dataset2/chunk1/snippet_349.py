#Source: https://stackoverflow.com/questions/37846721/django-typeerror-modelbase-object-is-not-iterable
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0003_auto_20160302_1749'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reputation',
            unique_together=set([('user', 'dimension')]),
        ),
    ]