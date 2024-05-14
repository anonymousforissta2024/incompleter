#Source: https://stackoverflow.com/questions/63704863/attributeerror-at-str-object-has-no-attribute-get-in-danjo
class Meta:
    model = HomePageModel
    fields = "__all__"

def clean(self):
    super(HomePageForm, self).clean()
    first_name = self.cleaned_data.get('first_name')
    try:
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        flag_decimal = 0
        flag_alpha = 0
        if len(first_name) > 20:
            raise ValidationError('Fisrt Name can not be more than 20 characters')
        if (regex.search(first_name) != None):
            raise ValidationError('Fisrt Name can not have a special character')
        else:
            for char in first_name:
                if char.isdecimal():
                    flag_decimal = 1
                if char.isalpha():
                    flag_alpha = 1
            if flag_decimal == 1 or flag_alpha == 0:
                raise ValidationError('Fisrt Name can not have a number')
        return first_name
    except ValidationError as e:
        print(e)