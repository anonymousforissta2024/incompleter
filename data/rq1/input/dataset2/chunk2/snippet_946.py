#Source: https://stackoverflow.com/questions/55509211/how-to-resolve-object-of-type-attributeerror-is-not-json-serializable
class InviteKeyCreateAllSerializer(serializers.ModelSerializer):
    current_user = serializers.SerializerMethodField('_user')
    is_take = serializers.SerializerMethodField()
    class Meta:
        model = Invite_Key
        exclude = [
            'user_submitter',
            'user_receiver',
            'uuid',
            'status',
            'is_taken',
            'is_locked',
            'claim_date',
            'expire_date',
        ]

    # Use this method for the custom field
    def _user(self, obj):
        request = getattr(self.context, 'request', None)
        if request:
            return request.user

    def get_is_taken(self, obj):
        return False

    def get_status(self, obj):
        return 'valid'

    # end of custom fields

    def create(self, validated_data):
        key = Invite_Key(
            user_submitter=validated_data['request.user'],
        )
        key.set_user_submitter(validated_data['user_submitter'])
        key.save()
        return key