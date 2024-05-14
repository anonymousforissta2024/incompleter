#Source: https://stackoverflow.com/questions/59848259/typeerror-int-object-is-not-iterable-serializer-django-serializer-for-one-to
class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = '__all__'


class TrailCompanySerializer(serializers.ModelSerializer):
    sectors = SectorSerializer(source="sector_id", many=True)

    class Meta:
        model = TrailCompany
        fields = '__all__'


class TrailSerializer(serializers.ModelSerializer):
    companies = TrailCompanySerializer(source="company_id", many=True)

    class Meta:
        model = Trail
        fields = '__all__'