#Source: https://stackoverflow.com/questions/53073447/attributeerror-module-has-no-attribute-while-avoiding-cyclic-reference-error
import model
import viewController
mModel = model.Model()
mVC = viewController.ViewController()
mModel.initializeApp(mVC)