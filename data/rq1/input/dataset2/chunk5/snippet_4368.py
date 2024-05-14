#Source: https://stackoverflow.com/questions/71683872/typeerror-entry-get-got-an-unexpected-keyword-argument-textvariable
long = tk.Entry(menu_add, text='Longitude', font=letter_font)
long_input = tk.Entry(menu_add, textvariable=long, font=letter_font)