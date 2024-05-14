#Source: https://stackoverflow.com/questions/58355894/typeerror-init-got-an-unexpected-keyword-argument-choices
class StudentMarksheetform2(forms.Form):
    subject_code=(
        (1,'CS101'),
        (2,'CS102'),
        (3,'CS103'),
        (4,'CS104'),
        (5,'CS105'),
        (6,'CS106')
    )
    code_title=forms.IntegerField(choices=subject_code,default='1')

    class Meta():
        model=StudentMarksheetdata2
        fields=['code_title']