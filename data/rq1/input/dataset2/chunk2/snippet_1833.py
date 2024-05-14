#Source: https://stackoverflow.com/questions/43328437/typeerror-object-of-type-categorymodel-is-not-json-serializable
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name