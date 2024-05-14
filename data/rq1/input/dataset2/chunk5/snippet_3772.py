#Source: https://stackoverflow.com/questions/60431962/django-attributeerror-when-trying-to-add-an-object-to-a-manytomanyfield
class AddFriendRedirect(RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        username = self.kwargs.get("username")
        obj = get_object_or_404(UserProfileInfo,slug=username)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.friends.all():
                obj.friends.remove(user)
                user.friends.remove(obj) # these are the fields causing the error
            else:
                obj.friends.add(user)
                user.friends.add(obj) # these are the fields causing the error
        return url_