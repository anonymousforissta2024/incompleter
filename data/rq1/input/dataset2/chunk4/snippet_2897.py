#Source: https://stackoverflow.com/questions/68633532/error-plz-help-i-am-getting-attribute-error-even-when-i-have-specified-the-datat
def subsets(inp,out,index):
    if index >= len(inp):
        print(out)
        return 
    subsets(inp,out,index+1)
    subsets(inp,out.append(inp[index]), index +1)
subsets([1,2,3],[],0)