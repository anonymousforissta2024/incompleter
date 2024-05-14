#Source: https://stackoverflow.com/questions/65727635/pandas-read-excel-new-string-type-error-when-passing-string-using-converters-p
df = pd.read_excel(xlsx_input_path, 'Sheet1', converters={"col_1": "string", "col_2": "string"}, engine="openpyxl")
print(f"9 -\n{df.dtypes}\n ")  # TypeError: 'str' object is not callable

df = pd.read_excel(xlsx_input_path, 'Sheet1', converters={"col_1": string, "col_2": string}, engine="openpyxl")
print(f"9 -\n{df.dtypes}\n ")  # NameError: name 'string' is not defined