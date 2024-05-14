#Source: https://stackoverflow.com/questions/53073447/attributeerror-module-has-no-attribute-while-avoiding-cyclic-reference-error
import model
class ViewController:
    def initialize(self, mod):
        self.model = mod