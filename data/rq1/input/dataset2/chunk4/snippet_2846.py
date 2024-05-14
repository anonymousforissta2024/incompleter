#Source: https://stackoverflow.com/questions/43535768/python-typeerror-int-object-is-not-iterable-in-selectmultiplefield-wtform
class AssignmentsForm(CSRFForm):
    responsible = SelectMultipleField(lazy_gettext("Select assignee"), choices=[])