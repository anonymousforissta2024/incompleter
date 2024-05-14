#Source: https://stackoverflow.com/questions/54620191/list-comprehension-returntypeerror-string-indices-must-be-integers
album_1974 = [row for row in album if row["Year"]=='1974'] 
print ("Number of albums released in 1974:", len(album_1974))