#Source: https://stackoverflow.com/questions/46750783/why-does-django-assertformerror-throw-a-typeerror-argument-of-type-property-i
class SessID(forms.Field):

    def validate(self, session_id):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(session_id)
        if len(session_id) < 32 > len(session_id):
            raise ValidationError(
                                  _('The Session ID needs to be exactly 32 characters long'),
                                  code = 'sessid wrong length'
                                  )
        if not re.match("^[A-Za-z0-9]*$", session_id):
            raise ValidationError(
                                  _('The Session ID should only have letters and numbers, no special characters'),
                                  code = 'sessid not alphanumeric'
                                  )        


class ResetSessID(forms.ModelForm):
    new_sessid = SessID()
    #forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '32'})                        )

    def __init__(self, *args, **kwargs):
        super(ResetSessID, self).__init__(*args, **kwargs)
        stdlogger.info("init of ResetSessID")
        #print("dir")#, self.fields.items['new_sessid'])
        if kwargs.get('instance'):
            new_sessid = kwargs['instance'].new_essid
            stdlogger.info("inner kwargs loop")
        return super(ResetSessID, self).__init__(*args, **kwargs)

    class Meta:
        model = PoeAccount
        exclude = ("acc_name", "sessid")

    def clean(self):
        if 'reg_button' in self.data:
            print("amazing")