#Source: https://stackoverflow.com/questions/44207149/django-save-to-db-typeerror-int-argument-must-be-a-string-a-bytes-like-obje
class InstagramAccount(models.Model):
    username = models.CharField(max_length=45, primary_key=True)
    password = models.CharField(max_length=45)
    account_id_account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account_id_account')
    expired_date = models.DateTimeField(null=False)
    history_of_payments = models.TextField(blank=True, null=True)
    account_type = models.TextField(default='trial')

    class Meta:
        managed = False
        db_table = 'instagram_account'
        unique_together = (('account_id_account', 'username'),)

class Proxy(models.Model):
    id_proxy = models.AutoField(primary_key=True)
    proxy = models.CharField(max_length=45, blank=False, null=False)
    meta = models.TextField(null=True)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=True)
    country = models.CharField(max_length=45, null=False)
    period = models.PositiveIntegerField()
    price = models.FloatField(validators=[MinValueValidator(0.0), ])
    # It can confuse, but our proxy provider have it own id for proxy
    proxy_provider_id = models.PositiveIntegerField()
    ip = models.CharField(max_length=45, null=False, blank=False)
    account = models.ForeignKey(InstagramAccount, models.DO_NOTHING,
                                db_column='instagram_account_account_id_account')

    class Meta:
        managed = False
        db_table = 'proxy'
        unique_together = (('id_proxy', 'account'),)