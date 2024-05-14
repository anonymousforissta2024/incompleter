#Source: https://stackoverflow.com/questions/61047626/best-way-to-deal-with-a-filenotfounderror
while True:
    try:
        with open("etalons.txt", "r") as fichier: 
            etalons = []
            for ligne in fichier:
               temp = ligne.split(',')
               ets = {
                       'conc' : temp[0],
                       'abs' :  temp[1]
                       }
               etalons.append(ets) # stockage des dicos dans liste
        break
    except FileNotFoundError:
        print("File not found. Check if the file is in the folder and it's name. ")
        time.sleep(20)