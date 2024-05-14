#Source: https://stackoverflow.com/questions/58902206/get-form-in-modeladmin-causing-typeerror
class CustomMemoAdmin(admin.ModelAdmin):
    form = AdminMemoForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
    #     if not request.user.is_superuser:
    #         self.fields = (
    #             'title',
    #             'content',
    #             'important',
    #             'receiver',
    #             'read',
    #             'unread',
    #             'word_file',
    #         )
    #     self.filter_horizontal = ('casino',)
        return form()