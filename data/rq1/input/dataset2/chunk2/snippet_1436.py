#Source: https://stackoverflow.com/questions/50707750/django-admin-stackedinline-not-loading-add-another-model-uncaught-typeerror-ca
@admin.register(models.Paper)
class PaperAdmin(BaseLiteratureAdmin):

    class EditedPaperAdminInline(admin.StackedInline):
        model = models.EditedPaper
        extra = 0

    class SupplementaryInformationAdminInline(admin.StackedInline):
        model = models.SupplementaryInformation
        extra = 0

    class PaperNotesAdminInline(BaseNotesAdminInline):
        exclude = tuple(
            i for i in BaseNotesAdminInline.exclude if i != 'paper'
        )

    class ReferencedPaperInline(admin.StackedInline):
        model = models.Paper.referenced_papers.through
        extra = 0
        fk_name = 'from_paper'
        verbose_name = "Referenced Paper"
        verbose_name_plural = "Referenced Papers"

    inlines = (
        EditedPaperAdminInline, # problem
        PaperNotesAdminInline, # ok single/together
        ReferencedPaperInline, # ok single/together
        SupplementaryInformationAdminInline, # problem
        
    )