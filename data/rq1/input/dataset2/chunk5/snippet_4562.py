#Source: https://stackoverflow.com/questions/55593541/getting-a-nameerror-in-an-if-else-statement-in-python-3
ld = 2
rd = 0
hd = 1
vhd = 1

if(rd>= 1):
    rt = (4*rd) + 2

elif(hd>=1 and rd==0):
    st = (4*hd + 2)

elif(ld>=1 and rd==0 and hd==0):
    lt = (4*ld + 2)

elif(ld>=1):
    lt = 4*ld

elif(hd>=1):
    st = hd

elif(vhd>=1):
    spt = vhd

else: 
    print('Error!')

print(spt)