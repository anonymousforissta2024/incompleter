#Source: https://stackoverflow.com/questions/43055952/typeerror-modelbase-is-not-iterable
from rest_framework import serializers
from offense_api.models import Season, Episode, Character


class SeasonSerializer(serializers.ModelSerializer):
    episodes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Season
        fields = ('season_number', 'episodes')


class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = ('episode_number', 'episode_title', 'episode_season')


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ('character_legal_first_name', 'character_legal_last_name', 'character_preferred_name',)