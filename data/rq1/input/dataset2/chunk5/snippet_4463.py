#Source: https://stackoverflow.com/questions/64098471/typeerror-for-dictionaries-unsupported-operand-types-for-int-and-str
ds = {'A': ['1', '3', '2', '5', '6'], 'B': ['1', '3', '2', '5'], 'C': ['3', '6', '8', '9', '7']} 

def analysis():
  lists = ds["A"]
  length = len(lists)
  print(lists)
  print(length)
  total = sum(lists)
  print(total)
 
analysis()