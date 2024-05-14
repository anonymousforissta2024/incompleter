#Source: https://stackoverflow.com/questions/50707750/django-admin-stackedinline-not-loading-add-another-model-uncaught-typeerror-ca
inlines = (
        PaperNotesAdminInline, # ok single/together
        ReferencedPaperInline, # ok single/together
        EditedPaperAdminInline, # problem
        SupplementaryInformationAdminInline, # problem
        
    )