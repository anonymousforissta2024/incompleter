#Source: https://stackoverflow.com/questions/54155083/name-error-when-reading-files-recursively-in-python3
top_dir_list= next(os.walk(root))[1]
for j in range(0,len(top_dir_list)):
    sub_src=top_dir_list[j]
    sub_root=os.path.join(root,sub_src)

    result_csv=os.path.join(sub_root,'metainfo.csv')
    with open(result_csv, 'w',encoding='utf-8') as csvfile:    
        fieldnames=['filename','duration','filesize']  # keys.
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
        csv_writer.writeheader()

        dirfiles=[]
        for path, subdirs, files in os.walk(sub_root):
            for item in files:
                dirfiles.append(os.path.join(path, item))
        length=len(dirfiles)
        for i in range(0,length):
            if dirfiles[i].endswith('.rar'):
                print('this is a rar file:', dirfiles[i])
            elif (dirfiles[i]).endswith(('mp3', 'wav')):
                #title=os.path.basename(dirfiles[i])
                title=tag.filesize
                tag = TinyTag.get(dirfiles[i])
                duration=tag.duration
                filesize=tag.filesize
            else:
                print("This file type is not supported:",dirfiles[i])

            csv_writer.writerow({'filename':title,'duration':duration,'filesize':filesize})