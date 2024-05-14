#Source: https://stackoverflow.com/questions/74169850/mongodb-with-django-typeerror-model-instances-without-primary-key-value-are-un
import uuid

from django.db import models


# Create your models here.
class ModernConnectUsers(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user_name = models.CharField(max_length=30, null=False)