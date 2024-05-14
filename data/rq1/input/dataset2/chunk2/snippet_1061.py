#Source: https://stackoverflow.com/questions/57940093/typeerror-init-missing-1-required-positional-argument-on-delete-djang
class FilerFileField(models.ForeignKey):
    default_form_class = AdminFileFormField
    default_model_class = File 

    def __init__(self, **kwargs):
        # We hard-code the `to` argument for ForeignKey.__init__
        dfl = get_model_label(self.default_model_class)
        if "to" in kwargs.keys():  # pragma: no cover
            old_to = get_model_label(kwargs.pop("to"))
            if old_to != dfl:
                msg = "%s can only be a ForeignKey to %s; %s passed" % (
                    self.__class__.__name__, dfl, old_to
                )
                warnings.warn(msg, SyntaxWarning)
        kwargs['to'] = dfl
        super(FilerFileField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {
            'form_class': self.default_form_class,
        }
        try:
            defaults['rel'] = self.remote_field
        except AttributeError:
            defaults['rel'] = self.rel
        defaults.update(kwargs)
        return super(FilerFileField, self).formfield(**defaults)