#Source: https://stackoverflow.com/questions/64190731/typeerror-at-init-got-an-unexpected-keyword-argument
class BidCreateView(LoginRequiredMixin, CreateView):
    
    model = Bid
    form_class = BidForm
    template_name = "auction/auction_detail.html"

    def get_context_data(self, **kwargs):
        bidder = self.request.user
        c = super().get_context_data(**kwargs)
        c["auction"] = self.auction
        if bidder.id is self.auction.user.id:
            c["form"] = None
        return c

    ###get_form_kwargs() method to supply user and listing during form creation
    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()
        pk_ = self.kwargs.get('pk')
        auction = Listing.objects.get(pk = pk_)
        kwargs = {
            'auction' : auction
        }

        return kwargs

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        bid_amount = form.cleaned_data["amount"]

        try:
            with transaction.atomic():
                Bid.high_bid(
                    self.auction,
                    self.request.user,
                    bid_amount
                )
        except IntegrityError:
            messages.error(self.request, "An unexpected error has occured")

        messages.success(self.request, "Bid submitted successfully!")

        return super().form_valid(form)