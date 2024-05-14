#Source: https://stackoverflow.com/questions/61619201/typeerror-bulk-create-got-an-unexpected-keyword-argument-ignore-conflicts
class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializerGroup(many=True, required=False)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')
        extra_kwargs = {
            'name': {'validators': []},
        }

    def create(self, validated_data):
        print(validated_data)
        permissions_data = validated_data.pop("permissions")
        obj, group = Group.objects.update_or_create(name=validated_data["name"])
        obj.permissions.clear()
        for permission in permissions_data:
            per = Permission.objects.get(codename=permission["codename"])
            obj.permissions.add(per)
        obj.save()
        return obj