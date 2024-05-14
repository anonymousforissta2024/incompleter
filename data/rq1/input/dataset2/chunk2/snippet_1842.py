#Source: https://stackoverflow.com/questions/61526938/filenotfounderror-errno-2-no-such-file-or-directory-cant-solve-a-path-prob
table_url = 'https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4'

table = 'table_' + table_url.split('/')[-1] + '.xlsx'
table_path = os.path.join(folder, table)
if not os.path.exists(table_path):
    books = pd.read_excel(table_url)
    # Save table
    books.to_excel(table_path)
else:
    books = pd.read_excel(table_path, index_col=0, header=0)