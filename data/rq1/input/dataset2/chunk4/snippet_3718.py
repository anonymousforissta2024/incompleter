#Source: https://stackoverflow.com/questions/46901151/typeerror-datetime-date-object-is-not-iterable
for p in (row):
    column_num = 1
    for item in  p:
        _ = ws0.cell(row=row_number, column=column_num, value=item)
        column_num = column_num + 1
        row_number = row_number + 1