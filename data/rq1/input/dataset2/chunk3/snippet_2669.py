#Source: https://stackoverflow.com/questions/62032946/drf-creating-new-objects-from-nested-representation-raises-typeerror
class Article(models.Model):
    uuid = models.UUIDField(editable=False, unique=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='article_company_id',
    )
    articleType = models.ForeignKey(
        ArticleType,
        on_delete=models.PROTECT,
        related_name='type',
    )    
    date_inserted = models.DateField()    
    def __str__(self):
        return self.uuid