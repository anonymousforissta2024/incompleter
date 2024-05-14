#Source: https://stackoverflow.com/questions/56798183/how-to-fix-attribute-error-when-using-pandas-in-python
with open('The Project- 6-21 E on leg arc test 1.csv', "r") as csvfile:

    colnames = [ 'sensor', 'x', 'y', 'z', 'azimuth', 'elevation', 'roll', 'timestamp']

    data = pd.read_csv('The Project- 6-21 E on leg arc test 1.csv', names = colnames)

    names = data.name.tolist()

    x = data.x.tolist()