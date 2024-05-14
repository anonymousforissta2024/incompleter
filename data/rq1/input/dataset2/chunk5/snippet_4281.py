#Source: https://stackoverflow.com/questions/49000930/django-attributeerror-tag-object-has-no-attribute-summary
class Summary(models.Model):

    question_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=False)
    cover_image = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag', related_name='summaries', blank=True)
    userProfileSummary = models.ManyToManyField('UserProfile', through='UserProfileSummary')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name_plural = "Summaries"