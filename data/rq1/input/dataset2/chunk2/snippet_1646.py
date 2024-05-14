#Source: https://stackoverflow.com/questions/58622983/attributeerror-after-processing-the-view
class SongDetailView(DetailView):
    model = Song
    template_name = 'song/song_detail.html'

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(song=self.object, user = self.request.user)
            vote_url = reverse('music:song_vote_create', kwargs={'song_id':vote.song.id})
            vote_form = SongVoteForm(instance=vote)
            ctx['vote_form'] = vote_form
            ctx['vote_url'] = vote_url
        return ctx

class SongVoteCreateView(View):
    form_class = SongVoteForm
    context = {}

    def get_success_url(self,**kwargs):
        song_id = self.kwargs.get('song_id')
        return reverse('music:song_detail', kwargs={'pk':song_id})

    def post(self,request,pk=None,song_id=None):
        user = self.request.user
        song_obj = Song.objects.get(pk=song_id)
        vote_obj,created = Vote.objects.get_or_create(song = song_obj,user = user) 
        vote_form = SongVoteForm(request.POST, instance=vote_obj)

        if vote_form.is_valid():
            new_vote = vote_form.save(commit=False)
            new_vote.user = self.request.user
            new_vote.save()
            return new_vote