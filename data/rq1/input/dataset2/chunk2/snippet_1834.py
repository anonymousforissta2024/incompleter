#Source: https://stackoverflow.com/questions/67958138/how-to-fix-attributeerror-nonetype-object-has-no-attribute-group
from googletrans import Translator, constants
from pprint import print


# init the Google API translator
translator = Translator()

# translate a spanish text to english text (by default)
translation = translator.translate("Hola Mundo")


print("{} ({}) --> {} ({})".format(translation.origin, translation.src, translation.text, translation.dest))