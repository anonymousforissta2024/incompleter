#Source: https://stackoverflow.com/questions/67946350/attributeerror-when-trying-to-created-nested-serializer-in-django-rest-framework
class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'number', 'name', 'set_id']

class SetSerializers(serializers.ModelSerializer):
    cards = CardSerializers()

    class Meta:
        model = Set
        fields = ['id', 'code', 'name', 'releaseDate','cards']