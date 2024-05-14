#Source: https://stackoverflow.com/questions/54966674/python-typeerror-object-of-type-user-is-not-json-serializable-after-upgrading
class TaggedArticle(models.Model):
    user = models.ForeignKey(User, related_name='tagging', on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    category_fit = models.CharField(choices=choices, max_length=255)
    article = models.ForeignKey(Article, related_name='articles', on_delete=models.CASCADE)
    link = models.URLField(max_length=255,)
    relevant_feedback = models.TextField(blank=True)
    category = models.CharField(max_length=255,)
    created_at = models.DateTimeField(default=timezone.now, editable=False)