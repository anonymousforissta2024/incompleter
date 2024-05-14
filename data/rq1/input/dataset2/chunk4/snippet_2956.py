#Source: https://stackoverflow.com/questions/63652709/django-import-export-import-error-attributeerror-str-object-has-no-attribu
created = models.DateTimeField(blank=True)
updated = models.DateTimeField(blank=True)
deleted_at = models.DateTimeField(blank=True,null=True)