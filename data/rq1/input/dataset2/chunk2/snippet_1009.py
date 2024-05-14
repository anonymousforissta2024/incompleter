#Source: https://stackoverflow.com/questions/73704946/typeerror-type-object-is-not-iterable-drf
from rest_framework import serializers
from .models import Movie, Actor, Reviews

class ActorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Actor
    fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reviews
    fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
  actors = ActorSerializer(many=True)
  average_reviews = serializers.SerializerMethodField()
  def get_average_reviews(self,obj):
    return obj.average_reviews()
  class Meta:
    model = Movie
    fields = '__all__'