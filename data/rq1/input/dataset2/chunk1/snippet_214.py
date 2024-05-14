#Source: https://stackoverflow.com/questions/57823653/typeerror-headers-is-an-invalid-keyword-argument-for-print
from tabulate import tabulate
i: int
with open("incre.txt", "w") as file:

    for i in range(1, 100,5):
        mol = int((i*50)/(i+50))
        file.write(str(i)+ " " +str(mol) + "\n")
    print(tabulate([[i], [mol]]), headers=['i' , 'mol'], tablefmt='orgtbl')
    file.close()