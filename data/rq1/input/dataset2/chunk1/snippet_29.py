#Source: https://stackoverflow.com/questions/65144681/attributeerror-nonetype-object-has-no-attribute-group-googletrans-python
from googletrans import Translator

text = 'hello'
translator = Translator()
result = translator.translate(text).src