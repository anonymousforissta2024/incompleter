#Source: https://stackoverflow.com/questions/52695868/serializers-django-rest-framework-attributeerror-got-attributeerror-when-att
class Keyword(models.Model):
    name=models.CharField(max_length=500,unique=True)
    image = models.ImageField(upload_to='keywords/', blank=True, null=True)
    mood=models.ManyToManyField(Mood,blank=True)
    def __str__(self):
        return str(self.name)

class UserKeyword(models.Model):
    keywords=models.ManyToManyField(Keyword)
    count=models.IntegerField(blank=True,null=True,default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)