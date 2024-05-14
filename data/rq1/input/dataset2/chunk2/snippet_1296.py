#Source: https://stackoverflow.com/questions/68685315/dynamic-serializer-django-rest-attributeerror-serializer-object-has-no-attr
class SNHUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNHUser
        fields = '__all__'


    user = UsersSerializer()


    def create(self, validated_data):
        # Create first the django user
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        # Create the layer of profile for the user
        return SNHUser.objects.create(user=user, **validated_data)


    def to_representation(self, obj):
        return super(SNHUserSerializer, self).to_representation(obj)