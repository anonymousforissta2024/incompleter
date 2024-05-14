#Source: https://stackoverflow.com/questions/52262519/typeerror-cannot-do-slice-indexing-on-class-pandas-core-indexes-base-index
import pandas as pd

#Reading Input File and converting into dataframe

input_data=pd.read_csv("C:\\Users\\hp\\Desktop\\py\\Input_Data.txt",delimiter =',') 
input_data_df=pd.DataFrame(input_data)


#Reading Reference File and converting into dataframe

reference_data=pd.read_csv("C:\\Users\\hp\\Desktop\\py\\Reference_Data.txt",delimiter =',') 
reference_data_df=pd.DataFrame(reference_data)



#Merging files based on unique Columns

Input_Reference_merge= pd.merge(input_data_df, reference_data_df, on=['emp_id', 'emp_name'])
print(Input_Reference_merge)


# Get the index where jan starts
months_index_start = input_data_df.columns.get_loc("jan")

# Calculate the total salary for each row according to the months_worked column

Input_Reference_merge["total_sal"] = Input_Reference_merge.apply(lambda x : x[months_index_start : months_index_start + x["months_worked"]].sum(), axis = 1)
print(Input_Reference_merge)