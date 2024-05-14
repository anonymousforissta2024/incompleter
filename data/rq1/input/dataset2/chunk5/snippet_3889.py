#Source: https://stackoverflow.com/questions/45462397/itertuples-in-tkinter-function-reveals-an-attributeerror-tuple-object-has-n
value = []; i = 0
for row in df.itertuples(): 
            i = 1 + i
            if i == 10: 
                value_app = row.A
                value.append(value_app)
                i=0