#Source: https://stackoverflow.com/questions/75170132/typeerror-int-object-is-not-subscriptable-dbscan
#retrieving the length and the breadth of the image
length = len(img)
breadth = len(img[0])
if (isdbscan):
    print("Number of clusters = ",maxclus)
    for a in range(0,length):
        for aa in range(0,breadth):
            #here we want to change all the outliners to black color  
            if (clusters[a][aa] == -1):
                img[a][aa][0]= 0
                img[a][aa][1]= 0
                img[a][aa][2]= 0
    for z in range(0,maxclus):
        #we randomly try to select the colors for the clusters 
        b = random.sample(range(0,255),1)
        bb = random.sample(range(0,255),1)
        bbb = random.sample(range(0,255),1)
        for a in range(0,length):
            for aa in range(0,breadth):
                if (clusters[a][aa] == z+1):
                    img[a][aa][0]= b[0]
                    img[a][aa][1]= bb[0]
                    img[a][aa][2]= bbb[0]