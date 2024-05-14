#Source: https://stackoverflow.com/questions/52140360/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type
class RequestItem(generic.CreateView):
    model = UserNotification
    fields = ['Name', 'Mobile_No', 'Proof']

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(UserNotification, self).get_form(form_class)
        form.fields['Name'].widget = TextInput(attrs={'placeholder': '*Enter your name'})
        form.fields['Mobile_No'].widget = TextInput(
            attrs={'placeholder': "*Enter your's mobile number to get a call back from angel"})
        form.fields['Proof'].widget = TextInput(attrs={'placeholder': '*enter proof you have for your lost item'})
        return form

    def form_valid(self, form):
        print(self.kwargs)

        self.object = form.save(commit=False)
        qs = Report_item.objects.filter(id=self.kwargs.get("pk"))
        self.object.user = qs[0].owner
        self.object.save()
        return HttpResponse("<h1>Your request has been processed</h1>")