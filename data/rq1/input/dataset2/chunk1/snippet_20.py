#Source: https://stackoverflow.com/questions/43924260/filenotfound-error-when-trying-to-move-files-with-the-shutil-python-module
import shutil, os

gifext = ['.gif', 'gifv']
picext = ['.png', '.jpg']

for file in files:
   if file.endswith(tuple(gifext)):
       if not os.path.exists(cdir+'\Gifs'):
           os.makedirs(cdir + '\Gifs')
       shutil.move(cdir + file, cdir + '\Gifs')

   elif file.endswith(tuple(picext)):
       if not os.path.exists(cdir+'\Images'):
           os.makedirs(cdir + '\Images')
       shutil.move(cdir + file, cdir + '\Images')