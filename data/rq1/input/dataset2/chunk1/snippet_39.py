#Source: https://stackoverflow.com/questions/35367340/importing-module-causes-typeerror-module-init-takes-at-most-2-arguments
from actions import ListitAction

class ViewAction(ListitAction):

    def __init__(self, view_id):
        ListitAction.__init__(self)
        self.view_id = view_id

    def build_uri():
        return "test"