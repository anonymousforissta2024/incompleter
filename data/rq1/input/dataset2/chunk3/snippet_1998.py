#Source: https://stackoverflow.com/questions/60381766/how-do-i-create-a-field-in-my-serializer-to-avoid-a-typeerror-cannot-unpack-no
class AddressTypeField(serializers.PrimaryKeyRelatedField):

    queryset = Address.objects

    def to_internal_value(self, data):
        if type(data) == dict:
            locality = data['locality']
            locality, created = Locality.objects.get_or_create(**locality)
            data['locality'] = locality
            address, created = Address.objects.create(**data)
            # Replace the dict with the ID of the newly obtained object
            data = address.pk
        return super().to_internal_value(data)
...

class CoopSerializer(serializers.ModelSerializer):
    type = CoopTypeField()
    address = AddressTypeField()

    class Meta:
        model = Coop
        fields = ['id', 'name', 'type', 'address', 'enabled', 'phone', 'email', 'web_site']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['type'] = CoopTypeSerializer(instance.type).data
        rep['address'] = AddressSerializer(instance.address).data
        return rep

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Coop.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Coop` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.address = validated_data.get('address', instance.address)
        instance.enabled = validated_data.get('enabled', instance.enabled)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.web_site = validated_data.get('web_site', instance.web_site)
        instance.save()
        return instance