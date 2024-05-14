#Source: https://stackoverflow.com/questions/67946350/attributeerror-when-trying-to-created-nested-serializer-in-django-rest-framework
class Set(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...

    objects = models.Manager()

    def __str__(self):
        return self.name

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...
    set = models.ForeignKey(Set, on_delete=models.CASCADE, related_name='Cards', related_query_name='Cards')


    objects = models.Manager()

    def __str__(self):
        return self.name