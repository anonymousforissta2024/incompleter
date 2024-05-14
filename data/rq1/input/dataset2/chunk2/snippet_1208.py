#Source: https://stackoverflow.com/questions/66003120/airflow-2-0-attributeerror-myoperator-object-has-no-attribute-kwargs
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

class MyOperator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 name,
                 *args,
                 **kwargs):
        super(MyOperator, self).__init__(*args, **kwargs)
        self.name = name

    def execute(self, context):

        return self.kwargs