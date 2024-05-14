#Source: https://stackoverflow.com/questions/58784123/one-to-one-relationship-how-to-fix-got-attributeerror-when-attempting-to-get-a
class ProfileSerializer (serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'image')