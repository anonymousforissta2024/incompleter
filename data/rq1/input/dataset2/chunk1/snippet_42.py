#Source: https://stackoverflow.com/questions/52675510/attributeerror-settings-object-has-no-attribute-auth-user-model-value-after
class Vote(models.Model):

    rate_type = models.BooleanField()
    question = models.ForeignKey("Question", related_name='question_rate', on_delete=models.PROTECT)
    answer = models.ForeignKey("Answer", related_name='answer_rate', on_delete=models.PROTECT)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)


    class Meta:
        unique_together = [('question', 'user'), ('answer', 'user'), ]