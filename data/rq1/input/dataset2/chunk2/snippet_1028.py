#Source: https://stackoverflow.com/questions/65701682/django-models-in-admin-return-typeerror-bad-operand-type-for-unary-str
from django.contrib import admin
from .models import CurrencyManagementAssetsModel

admin.site.register(CurrencyManagementAssetsModel)