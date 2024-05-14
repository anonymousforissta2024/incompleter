#Source: https://stackoverflow.com/questions/68415092/i-cant-understand-why-googletrans-in-python-isnt-working-it-gives-error-attr
from googletrans import Translator

translator = Translator() 

result = translator.translate('Mikä on nimesi', src='fi', dest='fr')

print(result.src)
 
print(result.dest)
 
print(result.text)