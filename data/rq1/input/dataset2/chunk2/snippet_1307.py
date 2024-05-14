#Source: https://stackoverflow.com/questions/43055952/typeerror-modelbase-is-not-iterable
from django.db import models


class Season(models.Model):
    season_created = models.DateTimeField(auto_now_add=True)
    season_number = models.IntegerField(unique=True)

    def __unicode__(self):
        return self.season_number

    def __str__(self):
        return str(self.season_number)


class Episode(models.Model):
    episode_season = models.ForeignKey(Season, related_name='episodes', on_delete=models.CASCADE)
    episode_created = models.DateTimeField(auto_now_add=True)
    episode_number = models.IntegerField()
    episode_title = models.CharField(max_length=300, default='')

    def __unicode__(self):
        return '%d. %d' % (self.episode_season.season_number, self.episode_number)

    def __str__(self):
        return '%d. %d' % (self.episode_season.season_number, self.episode_number)

    class Meta:
        unique_together = ('episode_season', 'episode_number')
        ordering = ('episode_number',)


class Character(models.Model):
    character_created = models.DateTimeField(auto_now_add=True)
    character_legal_first_name = models.CharField(max_length=50, default='', null=True)
    character_legal_last_name = models.CharField(max_length=100, default='', null=True)
    character_preferred_name = models.CharField(max_length=150, default='', primary_key=True)

    def __unicode__(self):
        return self.character_preferred_name

    def __str__(self):
        return self.character_preferred_name

    class Meta:
        ordering = ('character_preferred_name',)