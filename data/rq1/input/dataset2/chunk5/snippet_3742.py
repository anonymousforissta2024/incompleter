#Source: https://stackoverflow.com/questions/55293455/how-do-i-clear-the-unique-id-is-1-and-filenotfounderror
os.rename("C:\\Users\\finol\\Desktop\\ISRO\\Final Program\\OVERVIEW.OUT",
          str(uniqueid[a][0]))  ##The output file is renames with the uniqueid
import shutil

shutil.move(str(uniqueid[a][0]),
            "C:\\Users\\finol\\Desktop\\ISRO\\Final Program\\OUTPUT\\")  ##The output file is moved to a seperate directory
a = a + 1