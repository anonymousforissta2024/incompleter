#Source: https://stackoverflow.com/questions/53463416/django-attributeerror-int-object-has-no-attribute-save
class CreateEvent(IsVerifiedMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/event_form.html'

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        print(self.object.user.profile.total_events) #This prints 0
        self.object.user.profile.total_events += 1
        print(self.object.user.profile.total_events) # This prints 1
        self.object.user.profile.total_events.save() # If I don't use this statement it does not save to database. But It gives me the above error
        self.object.save()
        return super().form_valid(form)