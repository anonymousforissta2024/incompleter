#Source: https://stackoverflow.com/questions/73842091/attribute-error-object-has-no-attributes-while-trying-to-update-the-manytoo
class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ["watchlist"]
    


class WatchListSerializer(serializers.ModelSerializer):
    ### using relation serializer to list all the reviews in a movie 
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"