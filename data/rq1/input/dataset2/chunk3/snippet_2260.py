#Source: https://stackoverflow.com/questions/68146968/typeerror-tuple-indices-must-be-integers-or-slices-not-list
avgPetal_widthS = Average(petal_widthS)
avgPetal_widthVe = Average(petal_widthVe)
avgPetal_widthVi = Average(petal_widthVi)
avgPetal_lengthS = Average(petal_lengthS)
avgPetal_lengthVe = Average(petal_lengthVe)
avgPetal_lengthVi = Average(petal_lengthVi)
avgSepal_widthS = Average(sepal_widthS)
avgSepal_widthVe = Average(sepal_widthVe)
avgSepal_widthVi = Average(sepal_widthVi)
avgSepal_lengthS = Average(sepal_lengthS)
avgSepal_lengthVe = Average(sepal_lengthVe)
avgSepal_lengthVi = Average(sepal_lengthVi)

setosa = []
versicolor = []
virginica = []

setosa.append(['Setsota',avgPetal_lengthS,avgPetal_widthS,avgSepal_lengthS,avgSepal_widthS])
versicolor.append(['Versicolor',avgPetal_lengthVe,avgPetal_widthVe,avgSepal_lengthVe,avgSepal_widthVe])
virginica.append(['Virginica',avgPetal_lengthVi,avgPetal_widthVi,avgSepal_lengthVi,avgSepal_widthVi])

avgIris = (
    ['Setsota',avgPetal_lengthS,avgPetal_widthS,avgSepal_lengthS,avgSepal_widthS], 
    ['Versicolor',avgPetal_lengthVe,avgPetal_widthVe,avgSepal_lengthVe,avgSepal_widthVe],
    ['Virginica',avgPetal_lengthVi,avgPetal_widthVi,avgSepal_lengthVi,avgSepal_widthVi])

gap = ' '*3
heading = f"{'Species:':11s}{gap}{'Petal Length':12s}{gap}{'Petal Width':11s}{gap}{'Sepal Length':12s}{gap}{'Sepal Width':11s}"
print("\n")
print("="*69)
print(heading)
print("-"*69)
print("Attributes (cm):")
for i in avgIris:
    rec = f"{avgIris[i][0]:11s}{gap}{avgIris[i][1]:12f}{gap}{avgIris[i][2]:11f}{gap}{avgIris[i][3]:12f}{gap}{avgIris[i][4]:11f}"
print(rec)