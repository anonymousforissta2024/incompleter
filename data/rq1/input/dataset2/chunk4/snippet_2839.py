#Source: https://stackoverflow.com/questions/62032946/drf-creating-new-objects-from-nested-representation-raises-typeerror
class UserArticle(models.Model):    
    user = models.ForeignKey(User, to_field='user_id',
                             on_delete=models.PROTECT,)
    article = models.ForeignKey(Article, to_field='uuid',
                                 on_delete=models.PROTECT,)
    posted_as = ArrayField(
        models.CharField(max_length=100, blank=True),)
    post_date = models.DateField()

    class Meta:
        db_table = "core_user_articles"