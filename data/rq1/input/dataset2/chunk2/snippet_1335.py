#Source: https://stackoverflow.com/questions/53947049/attributeerror-at-login-type-object-super-has-no-attribute-save
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)