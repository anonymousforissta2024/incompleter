#Source: https://stackoverflow.com/questions/54381303/typeerror-type-combinedexpression-doesnt-define-round-method
class Article(models.Model):
    ...
    created_on = models.DateTimeField(default=datetime.now)