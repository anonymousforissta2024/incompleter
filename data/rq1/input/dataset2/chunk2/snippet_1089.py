#Source: https://stackoverflow.com/questions/65701682/django-models-in-admin-return-typeerror-bad-operand-type-for-unary-str
class CurrencyManagementAssetsModel(models.Model):
    RequestId = models.IntegerField(blank=False)
    CbnInstitutionCode = models.CharField(max_length=5, blank=False)
    SortCode = models.CharField(max_length=10, blank=False)
    Count = models.IntegerField(blank=False)
    AssetClassificationId = models.IntegerField(blank=False)
    AssetTypeId = models.IntegerField(blank=False)
    ValueOfCurrencyDistributed = models.DecimalField(max_digits='20', decimal_places='10', 
    blank=False)
    VaultCapacity = models.DecimalField(max_digits='20', decimal_places='10', blank=False)
    Year = models.IntegerField(blank=False)
    HalfOftheYear = models.IntegerField(blank=False)

    class Meta:
        verbose_name = 'Currency Management Assets'