#Source: https://stackoverflow.com/questions/53760038/python-typeerror-unsupported-operand-types-for-io-textiowrapper-and-s
today=datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
string_file="string_"+today+".csv"
outputFile = open(string_file_rdkb, "w")
#....some code here...
my_df=pd.DataFrame(datalist2)
my_df.to_csv(outputFile, index=False, header=False)
print(outputFile + " is generated") #Here is the issue