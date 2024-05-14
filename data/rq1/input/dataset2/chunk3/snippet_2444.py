#Source: https://stackoverflow.com/questions/58902206/get-form-in-modeladmin-causing-typeerror
class AdminMemoForm(forms.ModelForm):
    """
    Memo creation form, related to:

    :model: 'memos.Memo',
    """
    class Meta:
        model = Memo
        fields = (
            'title',
            'content',
            'important',
            'word_file',
            'receiver',
            'read',
            'unread',
        )