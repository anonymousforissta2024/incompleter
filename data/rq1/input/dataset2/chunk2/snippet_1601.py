#Source: https://stackoverflow.com/questions/49454529/django-forms-typeerror-init-got-an-unexpected-keyword-argument-instance
class ImpcalendarForm(forms.Form):
    establishment = forms.ModelChoiceField(queryset = Establishments.objects.all())
    page = forms.CharField(widget=forms.Textarea)
    pageold = forms.CharField(widget=forms.Textarea)
    change = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Impcalendar
        fields = '__all__'