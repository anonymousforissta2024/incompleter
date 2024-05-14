#Source: https://stackoverflow.com/questions/62803991/typeerror-when-trying-to-use-regex-on-pandas-dataframe
df['Product_Category'] = '-'
df['Product_Category'] = df['Product_Category'].apply(str)

prod_cat_ssd = re.compile(r'\bSOLIDO\b|\bSSD\b|\bSÃ³LIDO\b')
prod_cat_hdd = re.compile(r'\bDURO\b|\bRIGIDO\b|\bRÃ­GIDO\b|\bRIGIDOS\b|\bHDD\b')
prod_cat_external_ssd = re.compile(r'\b(EXTERNO|EXTREME)\b.*\b(SOLIDO|SSD|SÃ³LIDO)\b|\b(SOLIDO|SSD|SÃ³LIDO)\b.*\b(EXTERNO|EXTREME)\b')
prod_cat_external_hdd = re.compile(r'\b(EXTERNO|EXTREME)\b.*\b(DURO|RIGIDO|RIGIDOS|RÃ­GIDO|HDD)\b|\b(DURO|RIGIDO|RIGIDOS|RÃ­GIDO|HDD)\b.*\b(EXTERNO|EXTREME)\b')
df['Product_Category'] = df.apply(lambda row: 'SSD' if prod_cat_ssd.search(row.Titulo_Publicacion) else row.Product_Category, axis=1)
df['Product_Category'] = df.apply(lambda row: 'HDD' if prod_cat_hdd.search(row.Titulo_Publicacion) else row.Product_Category, axis=1)
df['Product_Category'] = df.apply(lambda row: 'External SSD' if prod_cat_external_ssd.search(row.Titulo_Publicacion) else row.Product_Category, axis=1)
df['Product_Category'] = df.apply(lambda row: 'External HDD' if prod_cat_external_hdd.search(row.Titulo_Publicacion) else row.Product_Category, axis=1)