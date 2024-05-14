#Source: https://stackoverflow.com/questions/68434807/typeerror-conversion-from-decimalfield-to-decimal-is-not-supported
class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"

class AuctionItem(models.Model):
    '''
    Description of Auction Item
    '''

    category_choices = [
        ("Fa", "Fashion"),
        ("To", "Toys"),
        ("Fo", "Food"),
        ("El", "Electronics"),
        ("Ho", "Home")
    ]

    title = models.CharField(max_length=16)
    description = models.CharField(max_length=128)
    image = models.URLField()
    category = models.CharField(max_length=16, choices=category_choices)
    create_time = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="owned")
    initial_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)

class BiddingPrice(models.Model):
    '''
    Bidding price of each item
    '''
    bid_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    auction_item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, null=True, related_name="bidding_price")

class Comments(models.Model):
    '''
    Comments made by different users
    '''
    comments = models.CharField(max_length=200)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="comments_given")
    connected_item = models.ManyToManyField(AuctionItem)