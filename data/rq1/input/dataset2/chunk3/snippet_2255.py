#Source: https://stackoverflow.com/questions/62032946/drf-creating-new-objects-from-nested-representation-raises-typeerror
class BatchUserArticleList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = UserArticle.objects.all()
    serializer_class = BatchUserArticleSerializer

    def create(self, request, *args, **kwargs):
        serializer = BatchUserArticleSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response({'Message': 'POST failed',
                                  'Errors': serializer.errors},
                                 status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)  # equal to serializer.save()
        return response.Response(serializer.data, status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)