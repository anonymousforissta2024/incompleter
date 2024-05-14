#Source: https://stackoverflow.com/questions/71422564/3d-volume-slicing-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-s
ini=p[0,0]
fin=p[0,:-1]
aux=img[:,:,ini.astype(int):fin.astype(int)]