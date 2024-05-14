#Source: https://stackoverflow.com/questions/66873968/filenotfounderror-errno-2-no-such-file-or-directory-corpus-or-ab-fmc-xlsx
dir = "/home/geta/kelo/eXP/Test/corpus"
for root, subdirs, files in os.walk(dir):
    print(root)
    for file in files:
        #print(files)
        print("-----File in processed :", file)
        # -----File in processed : corpus_or_AB_FMC.xlsx  # this file si located in the corpus directory
        sentences = pd.read_excel(file, sheet_name= 0)
        data_id = sentences.identifiant
        print("Total phrases: ", len(data_id))
        data = sentences.verbatim

        data_label = sentences.etiquette
        #print(type(data_id))
        #print(type(data))
        #number = LabelEncoder()
        # 0 = C; 1= F; 2= M
        #data_label = number.fit_transform(sentences.etiquette.astype('str'))
        #print(data_label)
        
        print("etiquette  :" , sentences['etiquette'].unique())
        classes = sentences['etiquette'].unique()
        len_classes = len(classes)