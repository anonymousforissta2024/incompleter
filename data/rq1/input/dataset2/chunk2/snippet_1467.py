#Source: https://stackoverflow.com/questions/58622983/attributeerror-after-processing-the-view
class VoteManager(models.Manager):

    def get_vote_or_unsaved_blank_vote(self,song,user):
        try:
            return Vote.objects.get(song=song,user=user)

        except ObjectDoesNotExist:
            return Vote.objects.create(song=song,user=user)

class Vote(models.Model):
    UP = 1
    DOWN = -1
    VALUE_CHOICE = ((UP, "👍️"),(DOWN, "👎️"),)


    like = models.SmallIntegerField(null=True, blank=True, choices=VALUE_CHOICE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    voted_on = models.DateTimeField(auto_now=True)

    objects = VoteManager()

    class Meta:
        unique_together = ('user', 'song')