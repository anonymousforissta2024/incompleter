#Source: https://stackoverflow.com/questions/73842091/attribute-error-object-has-no-attributes-while-trying-to-update-the-manytoo
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        ##posting the comment in a movie using movies primary key
        primary_key = self.kwargs.get("pk")
        watchlist = WatchList.objects.get(pk=primary_key)

        #NOt allowing the same user to comment on the same movie twice
        username = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, username=username)
        if review_queryset.exists():
            raise ValidationError("You cannot comment on the same movie Twice")

        ##NOTE: want to updated this section
        if watchlist.avg_rating == 0:
            watchlist.avg_rating = serializer.validated_data['avg_rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['avg_rating'])/2

        watchlist.num_rating += 1
        watchlist.avg_rating.save()
        serializer.save(watchlist=watchlist, username=username)