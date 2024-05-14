#Source: https://stackoverflow.com/questions/52786661/typeerror-in-string-requires-string-as-left-operand-not-float
import pandas as pd

data = pd.read_excel('C:/Users/my/Desktop/my_list.xlsx', 'Sheet1')
real_list = data['name'].tolist()