#Source: https://stackoverflow.com/questions/69516737/getting-a-type-error-at-articles-1-get-got-multiple-values-for-argument-id
class Article_List(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Bad Request


class ArticleDetails(APIView):
    def get_objects(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, id):
        article = self.get_objects(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request , id):
        article = self.get_objects(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id):
        article = self.get_objects(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)