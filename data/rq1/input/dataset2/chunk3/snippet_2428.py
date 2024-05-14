#Source: https://stackoverflow.com/questions/65727635/pandas-read-excel-new-string-type-error-when-passing-string-using-converters-p
df = pd.read_excel(xlsx_input_path, 'Sheet1',  engine="openpyxl")  
df = df.astype(dtype={"col_1": "string", "col_2": "string"})
print(f"6 -\n{df.dtypes}\n ")

df = pd.read_excel(xlsx_input_path, 'Sheet1', dtype={"col_1": "string", "col_2": str}, engine="openpyxl")
print(f"7 -\n{df.dtypes}\n ")

df = pd.read_excel(xlsx_input_path, 'Sheet1', converters={"col_1": str, "col_2": str}, engine="openpyxl")
print(f"8 -\n{df.dtypes}\n ") 