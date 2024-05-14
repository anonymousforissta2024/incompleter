#Source: https://stackoverflow.com/questions/62032946/drf-creating-new-objects-from-nested-representation-raises-typeerror
class User(models.Model):
    user_id = models.CharField(
        max_length=129,
        unique=True,
    )
    user_article = models.ManyToManyField(
        Article,
        through="UserArticle",
    )
    occupation = models.CharField(max_length=100, default='null')

    def __str__(self):
        return self.user_id