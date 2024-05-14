#Source: https://stackoverflow.com/questions/54380633/nameerror-name-f-is-not-defined-in-django-orm-query
class Article(models.Model):
    ...
    created_on = models.DateTimeField(default=datetime.now)