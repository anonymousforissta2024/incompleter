#Source: https://stackoverflow.com/questions/46050782/django-error-unsupported-operand-types-for-int-and-strtypeerror-at
class Ofac_Sdn(models.Model):
    number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    b_i = models.CharField(max_length=250, null=True)
    programe= models.CharField(max_length=250, null=True)

    more_info = models.CharField(max_length=250, null=True)
    vessel_call_sign = models.CharField(max_length=250, null=True)
    vessel_type= models.CharField(max_length=250, null=True)
    vessel_dwt = models.IntegerField(blank=True, null=True)
    tonnage = models.IntegerField(blank=True, null=True)
    vessel_flag = models.CharField(max_length=250, null=True)
    vessel_owner= models.CharField(max_length=250, null=True)
    dob_aka= models.CharField(max_length=250, null=True)