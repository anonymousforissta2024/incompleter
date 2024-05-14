#Source: https://stackoverflow.com/questions/69770023/python-colour-attributeerror-module-colour-has-no-attribute-ccs-illuminants
rgb = np.array([100, 80, 20]) / 255
xyz = colour.sRGB_to_XYZ(rgb)
lab = colour.XYZ_to_Lab(xyz)
print(lab) # 35, 4, 36