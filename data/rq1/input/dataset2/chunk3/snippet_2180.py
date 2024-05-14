#Source: https://stackoverflow.com/questions/56068629/how-to-fix-filenotfounderror-in-file-moving-script-when-it-reads-the-filenames
import shutil
import os
from pathlib import Path

assets_path = Path("/Users/Jackson Clark/Desktop/uploads")
export_path = Path("/Users/Jackson Clark/Desktop/uploads")

source = os.listdir(assets_path)

'''
NOTE: Filters.js is the important file
The logic:
    - Go through each file in the assets_path directory
    - Rename the files to start with RoCode (this could be a seperate script)
    - Create a new directory with the first four characters of the files name
    - Create two sub directories with the names 'image' and 'thumb'
    - Copy the file to both the 'image' and 'thumb' directories
    That should be all, but who knows tbh
Good links:
    - https://www.pythonforbeginners.com/os/python-the-shutil-module
    - https://stackabuse.com/creating-and-deleting-directories-with-python/
'''
for f in source:
    f_string = str(f)
    folder_one_name = f_string[0:2]
    folder_two_name = f_string[2:4]

    path_to_export_one = os.path.join(export_path, folder_one_name)
    path_to_export_two = os.path.join(export_path, folder_one_name,
                                      folder_two_name)

    try: 
        os.mkdir(path_to_export_one)
        os.mkdir(path_to_export_two)
        os.mkdir(os.path.join(path_to_export_two, "image"))
        os.mkdir(os.path.join(path_to_export_two, "thumb"))
        shutil.copy(f, os.path.join(path_to_export_two, "image"))
        shutil.copy(f, os.path.join(path_to_export_two, "thumb"))
    except FileExistsError as err:
        try:
            shutil.copy(f, os.path.join(path_to_export_two, "image"))
            shutil.copy(f, os.path.join(path_to_export_two, "thumb"))
        except FileNotFoundError as err:
            print("FileNotFoundError2 on " + f + " file")
    except FileNotFoundError as err:
        print("FileNotFoundError1 on " + f + " file")