#Source: https://stackoverflow.com/questions/56368432/typeerror-unhashable-type-collections-ordereddict
class ProfileSerializer(serializers.ModelSerializer):
    """Profile Serializer"""
    class Meta:
        model = Profile
        fields = ('user','profile_name','image','profile_title')
        extra_kwargs = {
            'image': {'read_only': True},
            'profile_name': {'read_only': True},
            'profile_title': {'read_only': True},
        }


class FriendsSerializer(serializers.ModelSerializer):
    """Serializer For Team Mambers"""
    members = ProfileSerializer(many=True)

    class Meta:
        model = Friend
        fields = '__all__'
    def create(self, validated_data):
        print(validated_data)
        user = validated_data['user']
        members = validated_data['members']

        instance = Friend.objects.create(user=user)
        instance.members.add(*members)
        return instance



class FriendsViewSet(ModelViewSet):
    """ViewSet For TeamMembers Model"""

    serializer_class = FriendsSerializer
    lookup_field = 'user'
    queryset = Friend.objects.all()


class Friend(models.Model):
    user = models.OneToOneField(User, related_name='creator', on_delete=models.CASCADE)
    members = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return str(self.user.username)