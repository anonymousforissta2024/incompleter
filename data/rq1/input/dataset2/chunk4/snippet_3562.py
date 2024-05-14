#Source: https://stackoverflow.com/questions/65160978/getting-nameerror-in-django-views-py-as-nameerror-name-edit-load-table-is
class facultyload(models.Model):
    empId = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    total_load = models.IntegerField()

    def __str__(self):
        return self.empId

class edit_load_table(models.Model):
    empId = models.CharField(max_length=20) 
    name = models.CharField(max_length=50)
    subject_abv = models.CharField(max_length=10)
    subject_load = models.IntegerField()
    subject_type = models.CharField(max_length=10)
    id_key = models.IntegerField()
    semester = models.CharField(max_length=20)
    
    def __str__(self):
        return self.empId