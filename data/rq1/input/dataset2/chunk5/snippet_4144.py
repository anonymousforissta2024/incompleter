#Source: https://stackoverflow.com/questions/42600875/python-typeerror-string-indices-must-be-integers
def parallelUpdateJSON(submatrix):
    with open('geo.geojson') as f:
        data = json.load(f)
    for feature in data: 
        currentfeature = submatrix[(submatrix['SId']==feature['properties']['cellId'])]
        if (len(currentfeature) > 0):
            feature['properties'].update({"style": {"opacity": currentfeature.AllActivity.item()}})
        else:
            feature['properties'].update({"style": {"opacity": 0}})


pool = Pool()
pool.map(parallelUpdateJSON, submatrix)
pool.close()
pool.join()