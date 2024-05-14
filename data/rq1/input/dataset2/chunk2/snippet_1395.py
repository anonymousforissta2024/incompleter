#Source: https://stackoverflow.com/questions/54620191/list-comprehension-returntypeerror-string-indices-must-be-integers
album_1974 = [row for row in album if is_valid_year(row["Year"]=="1974")] #this is list comprehension 
print ("No of album in 1974 released:",len(album_1974))