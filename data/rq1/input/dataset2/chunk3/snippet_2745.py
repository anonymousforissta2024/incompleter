#Source: https://stackoverflow.com/questions/47234130/typeerror-list-indices-must-be-integers-or-slices-not-str-when-using-nested-di
import textract, math, os
docs=[]
#Read the files and store them in docs
folder = os.listdir("./input/")
for file in folder:
    if file.endswith("txt"):
        docs.append ([file,textract.process("./input/"+file)])

inverted_index={}
for doc in docs:
    words=doc[1].decode()
    words=words.split(" ")

    #loop through and build the inverted index
    for word in words:
        temp={}
        #to remove initial white space
        if (word == " ") or (word==""):
            continue
        if word not in inverted_index:
            temp[doc[0]]=1
            temp['0']=0 #idf
            temp['1']=1 #tf
            inverted_index[word]=temp
        else:
            if doc[0] not in inverted_index[word].keys():
                inverted_index[word][doc[0]]=1
                inverted_index[word]['1']=inverted_index[word]['1']+1
            else:
                inverted_index[word][doc[0]]=inverted_index[word][doc[0]]+1

# to sort and print values with calculating the the tf and idf on the fly
for key, value in sorted(inverted_index.items()): # to sort words alphabitically
    inverted_index[key]=sorted(inverted_index[key]) # to sort the filenames where the word occured.
    inverted_index[key]['0']=math.log2(len(docs)/value['1']) # the error in this line
    print(key, value)