#Source: https://stackoverflow.com/questions/53073447/attributeerror-module-has-no-attribute-while-avoiding-cyclic-reference-error
import viewController
class Model():
    def initializeApp(self, viewContr: viewController.ViewController):
        self.vc = viewContr
        self.vc.initialize(self)