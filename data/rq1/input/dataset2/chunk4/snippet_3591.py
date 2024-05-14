#Source: https://stackoverflow.com/questions/74009860/how-do-i-fix-nameerror-in-python-i-defined-a-variable-in-a-for-loop-and-when-i
Carpeta = "C:/Users/Aguilar/datos de prueba" #directory

for subdirectorio in os.listdir(Carpeta):
    print(subdirectorio)


    for archivo in os.listdir(Carpeta+'/'+subdirectorio):
        if archivo.endswith(".lc"):
            print(archivo)
        
        
            # making data frame from csv file 
       
            data = pd.read_csv(Carpeta+'/'+subdirectorio+'/'+archivo, delimiter=' ', na_values='*********', usecols=[0,2,3], names = ['time', 'magnitude', 'error']) 

            # sorting by first name 
            data.sort_values('time', inplace = True) 

            # dropping ALL duplicate values 
            data.drop_duplicates(subset ="time", keep = False, inplace = True) 

            data = data[data['magnitude'].notna()]

            tess_lc_raw = data.to_records(index=False)