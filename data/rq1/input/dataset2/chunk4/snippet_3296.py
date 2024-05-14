#Source: https://stackoverflow.com/questions/73829248/unable-to-fetch-user-details-by-an-id-given-in-a-json-string-getting-a-type-er
from rest_framework import serializers
from users.models import Description, Team, User

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"