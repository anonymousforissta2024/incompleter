#Source: https://stackoverflow.com/questions/72692223/kivy-attributeerror-object-has-no-attribute-but-it-has
class TaskTemplate(BoxLayout, Button):
    task_name = StringProperty()
    def __init__(self):
        super(TaskTemplate, self).__init__()
        self.update_state = 'down'