import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row1_mean = row_mean[0]
print('Mean of Row 1 is', row1_mean)
row2_mean = row_mean[1]
print('Mean of Row 2 is', row2_mean)
row3_mean = row_mean[2]
print('Mean of Row 3 is', row3_mean)
column_mean = np.mean(arr, axis=0)
column1_mean = column_mean[0]
print('Mean of column 1 is', column1_mean)
column2_mean = column_mean[1]
print('Mean of column 2 is', column2_mean)
column3_mean = column_mean[2]
print('Mean of column 3 is', column3_mean)