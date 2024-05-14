#Source: https://stackoverflow.com/questions/66065071/got-attributeerror-when-attempting-to-get-a-value-for-field-text-on-serializer
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    post = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['text', 'created_at', 'post', 'owner']