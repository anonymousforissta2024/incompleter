#Source: https://stackoverflow.com/questions/54966674/python-typeerror-object-of-type-user-is-not-json-serializable-after-upgrading
class TagForm(forms.ModelForm):
    class Meta:
        model = TaggedArticle
        fields = ('user', 'category_fit', 'article', 'link', 'relevant_feedback', 'category',)
        widgets = {
            'category_fit': forms.RadioSelect()
        }