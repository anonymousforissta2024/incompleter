#Source: https://stackoverflow.com/questions/61432536/nameerror-name-pi-is-not-defined
cylinder_volume = Formula('PI * r**2 * h')
cylinder_volume('r= 1, h=2') .calc()