#Source: https://stackoverflow.com/questions/61432536/nameerror-name-pi-is-not-defined
triangle_hypotenuse = Formula('(a*a + b*b)**0.5')
print(triangle_hypotenuse('a=3, b=4') .calc())