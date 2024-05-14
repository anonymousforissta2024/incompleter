#Source: https://stackoverflow.com/questions/49000930/django-attributeerror-tag-object-has-no-attribute-summary
class Tag(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name