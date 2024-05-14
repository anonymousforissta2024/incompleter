#Source: https://stackoverflow.com/questions/71609574/my-code-is-not-working-typeerror-int-object-is-not-subscriptable
neword = '100115'
val=0
neword2=''
for n in range(0,len(neword),3):
  neword2 = chr(int(neword)[val]+int(neword)[val+1]+int(neword)[val+2])
  val+=3
print(neword2)