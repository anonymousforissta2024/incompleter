#Source: https://stackoverflow.com/questions/63678164/pandas-reset-index-gives-typeerror-cannot-compare-types-ndarraydtype-float64
df_all = pd.concat([pd.read_csv(file, header=None) for file in files])

files = ['https://raw.githubusercontent.com/sitrucp/who_vaccine_landscape/master/pdf_data/table-1.csv',
         'https://raw.githubusercontent.com/sitrucp/who_vaccine_landscape/master/pdf_data/table-2.csv',
         'https://raw.githubusercontent.com/sitrucp/who_vaccine_landscape/master/pdf_data/table-3.csv',
         'https://raw.githubusercontent.com/sitrucp/who_vaccine_landscape/master/pdf_data/table-4.csv',
         'https://raw.githubusercontent.com/sitrucp/who_vaccine_landscape/master/pdf_data/table-5.csv',
         'https://raw.githubusercontent.com/sitrucp/who_vaccine_landscape/master/pdf_data/table-6.csv',
         'https://raw.githubusercontent.com/sitrucp/who_vaccine_landscape/master/pdf_data/table-7.csv',
         'https://raw.githubusercontent.com/sitrucp/who_vaccine_landscape/master/pdf_data/table-8.csv',
         'https://raw.githubusercontent.com/sitrucp/who_vaccine_landscape/master/pdf_data/table-9.csv']