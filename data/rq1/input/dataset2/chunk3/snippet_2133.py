#Source: https://stackoverflow.com/questions/50194562/django-2-0-2-problems-with-modelform-creation-attributeerror-str-object-has
class RischiForm(ModelForm):
    class Meta:
        model = Rischi
        exclude = ['azienda', 'mansione']