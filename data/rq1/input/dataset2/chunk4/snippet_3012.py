#Source: https://stackoverflow.com/questions/63652709/django-import-export-import-error-attributeerror-str-object-has-no-attribu
edit_date = models.DateField(verbose_name="Edit Date", blank=True, default="1970-01-01")
premiere_date = models.DateField(verbose_name="Premiere Date", null=True, blank=True)