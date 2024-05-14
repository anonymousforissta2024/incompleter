#Source: https://stackoverflow.com/questions/76818922/typeerror-object-of-type-linkpreview-is-not-json-serializable
class PreviewLinkSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=255, required=True, allow_blank=False)