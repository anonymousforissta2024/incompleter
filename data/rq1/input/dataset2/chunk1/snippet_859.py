#Source: https://stackoverflow.com/questions/70564695/typeerror-unsupported-operand-types-for-float-and-decimal-decimal
class ExchangeRates(TimeStampedModel):
    date = models.DateField(unique=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    base_currency = models.CharField(max_length=10, default='GBP')
    data = JSONField()

    def get_currency_rate(self, currency):
        return Decimal(self.data[currency])

    def convert(self, from_currency, to_currency, value):
        from_rate = self.get_currency_rate(from_currency)
        to_rate = self.get_currency_rate(to_currency)


        return round((Decimal(value or 0) / from_rate) * to_rate, 6)