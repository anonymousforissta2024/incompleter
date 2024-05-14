#Source: https://stackoverflow.com/questions/42090620/typeerror-int-object-is-not-iterable-on-gresycale-image
if type(color)==int:
    color=(color,color,color)