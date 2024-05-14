#Source: https://stackoverflow.com/questions/52826653/classmethod-error-typeerror-call-takes-2-positional-arguments-but-3-wer
class MyModel(TimeStampedModel):
    some_field = models.CharField()

    @classmethod
    def my_class_method(cls, value, other_value):
        print(value)