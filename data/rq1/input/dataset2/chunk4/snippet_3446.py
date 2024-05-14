#Source: https://stackoverflow.com/questions/69555882/type-error-init-requires-1-positional-argument-yet-2-are-given
class change_about(UpdateView):
 def get_object(self, queryset=None):

     return User.objects.get(user=self.request.user)

 def form_valid(self, form):

     instance = form.instance # This is the new object being saved
     instance.user = self.request.user
     instance.save()

     return super(change_about, self).form_valid(form)