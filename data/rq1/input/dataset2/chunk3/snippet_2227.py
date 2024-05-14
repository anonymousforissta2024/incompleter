#Source: https://stackoverflow.com/questions/56353632/attributeerror-at-files
class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

class FileUp(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.FileField(upload_to='path')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name.name