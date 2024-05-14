#Source: https://stackoverflow.com/questions/34593638/filenotfounderror-when-creating-new-file
import os

for dirname, dirs, filename in os.walk("."):
    for file in filename:
        thefile = os.path.join(dirname,file)
        source = open(thefile,'rb')
        data = source.read()
        source.close()
        Newpath = "C:\\Users\kemburaj.kemburaj-PC\Documents\\backup\\" #paste the backup directory path, please check escape characters
        if not os.path.exists(Newpath):
            os.makedirs(Newpath)
        file = os.path.join(Newpath,thefile[2:]) #copy this py file in the directory which is to be backed up
        print(file)
        fhand = open(file,'wb')
        fhand.write(data)
        fhand.close()
        print("\n\nBackup >",file)