#Source: https://stackoverflow.com/questions/34500870/filenotfounderror-when-creating-a-file-using-a-variable-in-python-3-5-1
a, b = time.strftime("%d/%m/%Y"), time.strftime("%H-%M-%S")
c = ("SCORE"+"-"+"("+a+")"+"-"+"("+b+")")
c = str(c+".txt")