#Source: https://stackoverflow.com/questions/51768654/django-typeerror-at-account-register-tuple-object-is-not-callable
class RegisterView(CreateView):
    model = User, UserProfile
    form_class = RegistrationForm, UserProfileForm

    def post(self, request, *args, **kwargs):
        user_form = RegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_photo' in request.FILES:
                profile.profile_photo = request.FILES['profile_photo']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
        else:
            user_form = RegistrationForm()
            profile_form = UserProfileForm()

        return render(request, 'accounts/registration.html',
                      {'user_form': user_form, 'profile_form': profile_form, 
        'registered': registered})