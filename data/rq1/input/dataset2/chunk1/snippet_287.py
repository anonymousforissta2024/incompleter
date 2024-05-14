#Source: https://stackoverflow.com/questions/37846721/django-typeerror-modelbase-object-is-not-iterable
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def dedupe_reputation_actions(apps, schema_editor):
    Reputation = apps.get_model('reputation', 'Reputation')

    qs = Reputation.objects.all().values('user', 'dimension')\
        .annotate(total=models.Count('user'))\
        .filter(total__gt=1)

    for dupe in qs:
        reps = list(Reputation.objects.filter(user=dupe['user'], dimension=dupe['dimension']))

        for rep in reps[1:]:
            rep.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0002_auto_20151117_1108'),
    ]

    operations = [
        migrations.RunPython(dedupe_reputation_actions)
    ]