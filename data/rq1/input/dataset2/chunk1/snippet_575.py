#Source: https://stackoverflow.com/questions/65012433/identifying-location-of-error-typeerror-nonetype-object-is-not-subscriptable
from models import ToDoModel


class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        self.model.create(params["Title"], params["Description"])