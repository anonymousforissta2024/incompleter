#Source: https://stackoverflow.com/questions/66065071/got-attributeerror-when-attempting-to-get-a-value-for-field-text-on-serializer
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, queryset = None, **kwargs):
        item = self.kwargs.get('pk')
        return get_list_or_404(Comment, post = item)

    def get_queryset(self):
        return Comment.objects.all()