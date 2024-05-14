#Source: https://stackoverflow.com/questions/60258163/nameerror-name-model-is-not-defined-after-importing-models-in-a-newly-created
from django.utils import timezone
from django_smalluuid.models import SmallUUIDField, uuid_default
from django.db import models
import pytz
from .utilities import (calc_expiry_date,convert_date)
from monthdelta import monthdelta


class LiquorCostCentre(models.Model):
    cost_centre_id = models.CharField(max_length=250,null=True,blank=True,default="0304-05-05")
    cost_centre_name = models.CharField(max_length=250,null=True,blank=True)