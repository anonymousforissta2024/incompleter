#Source: https://stackoverflow.com/questions/52695868/serializers-django-rest-framework-attributeerror-got-attributeerror-when-att
class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields ='__all__'

class UserKeywordSerializer(serializers.ModelSerializer):
    keywords = KeywordsSerializer( read_only=True,many=True)

    class Meta:
        model = UserKeyword
        fields = '__all__'