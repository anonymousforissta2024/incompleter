#Source: https://stackoverflow.com/questions/52789603/typeerror-int-object-is-not-callable-in-python-3-when-calling-logging-info
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(message)s')

class employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last

        logging.INFO('Employee created: {} - {} '.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1=employee('John','Doe')
emp_2=employee('John','Smith')