#Source: https://stackoverflow.com/questions/46057819/attribute-error-method-object-has-no-attribute
class Item(models.Model):
    titel = models.CharField(max_length=200)
    omschrijving = models.TextField()
    aantal = models.IntegerField()