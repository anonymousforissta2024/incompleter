#Source: https://stackoverflow.com/questions/73842091/attribute-error-object-has-no-attributes-while-trying-to-update-the-manytoo
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    avg_rating = models.FloatField(default=0)
    num_rating = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment