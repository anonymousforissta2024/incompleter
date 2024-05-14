#Source: https://stackoverflow.com/questions/70054419/attributeerror-index-object-has-no-attribute-replace
dfpivot.columns=dfpivot.columns.str.replace("(","").replace(")","")
dfpivot.columns = dfpivot.columns.str.split(',', expand=True)