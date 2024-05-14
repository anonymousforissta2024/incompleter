#Source: https://stackoverflow.com/questions/76359431/typeerror-in-django-float-argument-must-be-a-string-or-a-number-not-tuple
class Order(models.Model):

    coin = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)
    bought_price = models.FloatField()
    quantity = models.IntegerField(default=1)
    bought_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)