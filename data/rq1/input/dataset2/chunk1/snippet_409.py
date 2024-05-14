#Source: https://stackoverflow.com/questions/42751642/py2neo-v3-attributeerror-object-has-no-attribute-db-exists
for row in data:    
    ds = DataSource()
    #   parse Source of Information column as a list, trimming whitespace
    ds.uri = list(map(str.strip, row['data_source'].split(',')))
    ds.description = row['data_source_description']
    graph.merge(ds)