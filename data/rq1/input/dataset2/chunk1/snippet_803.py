#Source: https://stackoverflow.com/questions/30953615/typeerror-object-is-not-json-serializable-in-django-1-8-python-3-4
class GreenBased(models.Model):
    NumOfStudents = models.CharField(max_length=300,blank=True)
    Green = models.CharField(max_length=300,blank=True)
    class Meta:
        managed = False
        db_table = "GreenStats"

class YelloBased(models.Model):
    NumOfStudents = models.CharField(max_length=300,blank=True)
    Yellow = models.CharField(max_length=300,blank=True)
    class Meta:
        managed = False
        db_table = "YellowStats"