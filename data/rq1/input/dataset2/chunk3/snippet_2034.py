#Source: https://stackoverflow.com/questions/67946350/attributeerror-when-trying-to-created-nested-serializer-in-django-rest-framework
class SetsIndividualData(ListAPIView):
    serializer_class = SetSerializers

    def get_queryset(self):
        setCode = self.kwargs.get('setCode')
        queryList = Set.objects.filter(code=setCode.upper())
        return queryList