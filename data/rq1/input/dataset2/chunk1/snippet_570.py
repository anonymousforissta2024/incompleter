#Source: https://stackoverflow.com/questions/38836795/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
class Stats(models.Model):
    user = models.OneToOneField('auth.User')
    views = models.IntegerField()
    visits = models.IntegerField()
    unique_visits = models.IntegerField()