#Source: https://stackoverflow.com/questions/56553165/how-to-fix-typeerror-catg-id-is-an-invalid-keyword-argument
class Choice(models.Model):
    chname = models.ForeignKey(Product, on_delete=models.CASCADE)
    chn = models.CharField(max_length=1000, default=" ")


    def __str__(self):
        return self.chn