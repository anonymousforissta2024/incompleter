#Source: https://stackoverflow.com/questions/56381315/attribute-errormodule-mysql-has-no-attribute-connector
import mysql.connector
import random
first_names=['Jodee,Marielle,Phillip,Colby,Stephany,Dione,Grover,Napoleon,Nicholas,Alysa,Noma,Leta,Ciera,Donny,Buc,Iren,Renato,Glory,Stacia,Bennie,Soo,Mitzie,Kaci,Peggy,Hilma,Melva,Cindie,Miyoko,Melina,Cammy,Blanche,Rhea,Jill,Kellye,Ailene,Vida,Alva,Sau,Hollis,Oswaldo,Marty']
last_names=['Bula,Bibi,Rolf,Tayna,Ardith,Art,Jeannetta,Patrina,Ronny,Maida,Cleopatra,Sherry,Vincenza,Sheri,Sherlyn,Shayne,Geneva,Javier,Celine,Saran,Shari,Boris,Gwyneth,Summer,Maryellen,Rufina,Essie,Palma,Rafael,Cordell,Jude,Jenine,Manuel,Cleveland,Daphine,Lavina,Candi,Rossie,Brunilda,Gilberte,Nick,Hoyt,Lucius,Ardis,Tyler,Dwain,Caleb,Aide,Mckinley,Margurite']
mydb=mysql.connector.connect(host='localhost',user='root',passwd='hariom21feb',database='test')
mycursor=mydb.cursor()
fkey=random.randint(0,49)
lkey=random.randint(0,49)
nkey=random.randint(0,50)
for i in range(nkey):
    query=('insert into test value(%s,%s,%s,%s,%s)')
    tup=('L5W4NW',first_names(fkey),last_names(lkey),'2970','completed')
    mycursor.execute(query,tup)
mydb.commit()