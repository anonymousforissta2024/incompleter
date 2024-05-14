#Source: https://stackoverflow.com/questions/46050782/django-error-unsupported-operand-types-for-int-and-strtypeerror-at
from django.contrib import admin

from ofac_sdn.models import Ofac_Sdn
from ofac_sdn.models import Ofac_Add
from ofac_sdn.models import Ofac_Alt
# Register your models here.    
admin.site.register(Ofac_Sdn)    
admin.site.register(Ofac_Add)
admin.site.register(Ofac_Alt)