#Source: https://stackoverflow.com/questions/57515323/attributeerror-tuple-object-has-no-attribute-get
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'subtitle', 'image', 'description', 'status']

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Titulo'}),
            'subtitle': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Subtitulo'}),
            'image': forms.FileInput(attrs = {'class': 'custom-file-input'}),
            'description': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Descripcion'}),
            'status': forms.Select(attrs = {'class': 'custom-select'}),
        }

        labels = {'title': '', 'subtitle': '', 'image': '', 'description': ''}

    def __init__(self, *args, **kwargs):
        self.title_valid = False 
        if 'title_valid' in kwargs:
            self.title_valid = kwargs.pop('title_valid')

        super().__init__(args, kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if self.title_valid:
            if Course.objects.filter(title = title).exists():
                raise forms.ValidationError('Ya existe un curso registrado con ese titulo, elige otro.')

        return title