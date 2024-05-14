#Source: https://stackoverflow.com/questions/71683872/typeerror-entry-get-got-an-unexpected-keyword-argument-textvariable
long = tk.Label(menu_add, text='Longitude', font=letter_font)
long_input = Entry.get(menu_add, textvariable=long, font=letter_font)