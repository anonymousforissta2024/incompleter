#Source: https://stackoverflow.com/questions/69770023/python-colour-attributeerror-module-colour-has-no-attribute-ccs-illuminants
rgb = np.array([100, 80, 20]) / 255
D50 = colour.CCS_ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['D50']
xyz = colour.sRGB_to_XYZ(rgb, illuminant=D50)
print(colour.XYZ_to_Lab(xyz, illuminant=D50))