#Source: https://stackoverflow.com/questions/53463416/django-attributeerror-int-object-has-no-attribute-save
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_events = models.IntegerField(default=0) 

class Event(models.Model):
    user = models.ForeignKey(User, related_name='seller')
    ...