#Source: https://stackoverflow.com/questions/57375527/success-redirect-to-profile-form-gives-typeerror-at-profile-join-argument
class UserProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileChangeForm
    success_url = reverse_lazy("user_profile:profile")
    # success_url = "/success/"
    success_message = "Profile updated"

    def get_object(self, *args, **kwargs):
        return self.request.user

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()

        return render(request, self.template_name, {"form": form})