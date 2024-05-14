#Source: https://stackoverflow.com/questions/59939620/attributeerror-postdetailview-object-has-no-attribute-method
class Post(models.Model):
    title = models.CharField(max_length=20)
    content =  models.TextField()
    date_posted = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)