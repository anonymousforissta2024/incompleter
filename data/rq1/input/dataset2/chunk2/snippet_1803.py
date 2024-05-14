#Source: https://stackoverflow.com/questions/61232050/typeerror-numpy-bool-object-is-not-iterable
import numpy as np


def rad_to_deg(x):
    deg = x*180/np.pi
    return deg

def flag_PA(x,bornes_test):  
    index_0_test = int(np.where(bornes_test==0)[0][0])
    for i in range(index_0_test):
        cond1 = any(bornes_test[i] <= x < bornes_test[i+1])
        cond2 = any(bornes_test[i]+180 <= x < bornes_test[i+1]+180)
        if np.logical_or(cond1,cond2)==True :
            flag_test=i 
    return flag_test


##################################### DATA READING ###########################

# Trouver les fichiers en Bande L et Bande N 


bornes_PA = np.linspace(-180,180,18+1)

lambda_fichier       = np.linspace(3E-6,11E-6)
u_coord_fichier      = np.linspace(1,40)
v_coord_fichier      = np.linspace(1,40)
baseline_fichier     = np.sqrt(np.array(u_coord_fichier)**2+np.array(v_coord_fichier)**2).tolist()
for l in range(len(lambda_fichier)):
    for b in range(len(baseline_fichier)):
        deg = rad_to_deg(np.arctan2(u_coord_fichier[b],v_coord_fichier[b]))
        result = int(flag_PA(deg,bornes_PA))