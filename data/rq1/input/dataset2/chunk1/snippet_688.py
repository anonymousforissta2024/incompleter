#Source: https://stackoverflow.com/questions/52469341/django-attribute-error-datetime-timedelta-object-has-no-attribute-decode
class CartSerializer(serializers.ModelSerializer):
    class Meta:
         model = TblCarts
         fields = '__all__'