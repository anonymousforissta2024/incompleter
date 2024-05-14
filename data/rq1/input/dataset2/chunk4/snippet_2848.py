#Source: https://stackoverflow.com/questions/71710269/reading-data-from-a-csv-file-yields-typeerror
import numpy as np
uncov_users = np.genfromtxt('ucov_users.csv', delimiter=',')
for i,j in uncov_users:
    ux_coor = i  
    uy_coor = j  
    print(ux_coor,uy_coor)