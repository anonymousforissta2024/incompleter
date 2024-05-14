#Source: https://stackoverflow.com/questions/52469341/django-attribute-error-datetime-timedelta-object-has-no-attribute-decode
class GetCarts(generics.ListAPIView):
     serializer_class = CartSerializer
     queryset = TblCarts.objects.all()