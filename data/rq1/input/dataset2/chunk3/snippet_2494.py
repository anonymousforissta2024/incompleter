#Source: https://stackoverflow.com/questions/58314475/django-typeerror-listserializer-object-is-not-iterable
class KeyboardEvent(models.Model):
    value = models.CharField(max_length=15)
    time = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(UserData,on_delete=models.CASCADE)
    def __str__(self):
        return self.value