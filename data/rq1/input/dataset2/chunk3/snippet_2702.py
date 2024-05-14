#Source: https://stackoverflow.com/questions/60221512/how-to-solve-the-problem-of-type-error-in-django
class NewsletterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email