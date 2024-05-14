#Source: https://stackoverflow.com/questions/72127203/typeerror-unsupported-operand-types-for-float-and-float-pandas
def que_fn(x,cols):

    if (x[(x[cols[2]]==x[cols[3]])]) & (x[x[cols[2]].notna()]) & (x[x[cols[3]].notna()]):   
        return "Test1"
    elif (x[x[cols[2]].isnull()]) & (x[x[cols[3]].isnull()]):
        return "Test1"
    elif (x[x[cols[2]].isnull()]) & (x[x[cols[3]].notna()]):
        return "Test2"
    elif (x[x[cols[2]].notna()]) & (x[x[cols[3]].isnull()]):
        return "Test3"
    else:
        return "Test4"
        
        
check_cols = ['id_a','id_b','value_a','value_b']

new_df['calc_value'] = test_df.apply(que_fn(test_df,check_cols),axis=1)